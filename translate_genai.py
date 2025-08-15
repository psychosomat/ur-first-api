# translate_genai.py
from __future__ import annotations
import argparse
import os
import re
import sys
import time
import textwrap
from pathlib import Path
from typing import List
import traceback
import certifi
import ssl

# Официальный SDK
from google import genai

# --- Конфиг по умолчанию ---
DEFAULT_MODEL = "gemini-2.5-flash"   # можно менять (gemini-2.5-pro, gemini-1.5-flash и т.д.)
DEFAULT_MAX_CHARS = 10000             # размер чанка (символы). Меняй при необходимости.
RETRY_DELAYS = [0, 2, 6]             # задержки между ретраями (с)

# --- Подсказка / правила перевода ---
SYSTEM_INSTRUCTIONS = textwrap.dedent("""
You are a meticulous professional technical translator.
Task: Translate the provided Markdown content from Russian to Korean.

Important rules:
- Preserve all Markdown formatting (headings, lists, tables, links, code fences) exactly.
- Translate prose, link text, comments inside code blocks (//, #, /* */, <!-- -->), docstrings and user-facing strings.
- Do NOT alter code syntax, identifiers, file paths, or URLs.
- Keep fenced code blocks (``` or ~~~) intact; do not add or remove fences.
- Output only the translated Markdown snippet (no extra commentary).
""").strip()

ANSI_RE = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")

def strip_ansi(s: str) -> str:
    return ANSI_RE.sub("", s)

def chunk_markdown(text: str, max_chars: int) -> List[str]:
    """
    Безопасное разбиение: не рвёт кодовые блоки и старается резать по логическим блокам.
    """
    parts: List[str] = []
    buf: List[str] = []
    in_fence = False
    fence_token = None

    for line in text.splitlines(keepends=True):
        fence_match = re.match(r"^(```|~~~)", line)
        if fence_match:
            tok = fence_match.group(1)
            if not in_fence:
                in_fence = True
                fence_token = tok
            elif tok == fence_token:
                in_fence = False
                fence_token = None

        buf.append(line)
        # нас интересуют естественные границы — пустая строка или заголовок вне кода
        if not in_fence and (line.strip() == "" or line.lstrip().startswith("#")):
            parts.append("".join(buf))
            buf = []
    if buf:
        parts.append("".join(buf))

    # теперь упакуем в чанки по max_chars
    chunks: List[str] = []
    cur: List[str] = []
    cur_len = 0
    for p in parts:
        if len(p) > max_chars:
            # если часть слишком велика (например огромный код), режем по строкам
            lines = p.splitlines(keepends=True)
            tmp: List[str] = []
            tmp_len = 0
            for ln in lines:
                if tmp and tmp_len + len(ln) > max_chars:
                    chunks.append("".join(tmp))
                    tmp = []
                    tmp_len = 0
                tmp.append(ln)
                tmp_len += len(ln)
            if tmp:
                chunks.append("".join(tmp))
        else:
            if cur and cur_len + len(p) > max_chars:
                chunks.append("".join(cur))
                cur = []
                cur_len = 0
            cur.append(p)
            cur_len += len(p)
    if cur:
        chunks.append("".join(cur))
    return chunks

def build_prompt(snippet: str) -> str:
    return textwrap.dedent(f"""
{SYSTEM_INSTRUCTIONS}

Translate the following snippet to Korean. Output only the translated Markdown.

---BEGIN SNIPPET---
{snippet}
---END SNIPPET---
""").strip()

def init_client(use_vertex: bool) -> genai.Client:
    print(f"[DEBUG] init_client: use_vertex={use_vertex}")
    try:
        if use_vertex:
            project = os.environ.get("GOOGLE_CLOUD_PROJECT")
            location = os.environ.get("GOOGLE_CLOUD_LOCATION")
            print(f"[DEBUG] project={project}, location={location}")
            if not project or not location:
                raise RuntimeError("Для Vertex AI нужны переменные GOOGLE_CLOUD_PROJECT и GOOGLE_CLOUD_LOCATION!")
            client = genai.Client(vertexai=True, project=project, location=location)
        else:
            api_key = os.environ.get("GEMINI_API_KEY")
            print(f"[DEBUG] api_key={'set' if api_key else 'not set'}")
            if not api_key:
                raise RuntimeError(
                    "GEMINI_API_KEY не найден в окружении! Получите ключ на https://aistudio.google.com/app/apikey и установите переменную окружения GEMINI_API_KEY.\n"
                    "Пример (Windows): set GEMINI_API_KEY=ваш_ключ"
                )
            # Проверка наличия certifi и файла сертификатов
            try:
                import platform
                ca_path = certifi.where()
                print(f"[DEBUG] certifi.where(): {ca_path}")
                print(f"[DEBUG] certifi version: {getattr(certifi, '__version__', 'unknown')}")
                print(f"[DEBUG] Python version: {platform.python_version()}")
                if not os.path.exists(ca_path):
                    raise FileNotFoundError(f"Файл сертификата не найден: {ca_path}")
                # Проверяем чтение файла
                with open(ca_path, "rb") as f:
                    data = f.read()
                    if not data:
                        raise RuntimeError(f"Файл сертификата пуст: {ca_path}")
                print(f"[DEBUG] certifi CA file size: {len(data)} bytes")
                # Пробуем создать ssl context явно (для отладки)
                _ = ssl.create_default_context(cafile=ca_path)
                # Выводим переменные окружения SSL
                for k in ["SSL_CERT_FILE", "REQUESTS_CA_BUNDLE", "CURL_CA_BUNDLE"]:
                    v = os.environ.get(k)
                    print(f"[DEBUG] env {k}: {v}")
            except Exception as e:
                raise RuntimeError(f"Проблема с SSL/certifi: {e}\nПопробуйте переустановить certifi: pip install --upgrade certifi\n"
                                 f"certifi.where(): {ca_path}\n"
                                 f"certifi version: {getattr(certifi, '__version__', 'unknown')}\n"
                                 f"Python version: {platform.python_version()}\n"
                                 f"env SSL_CERT_FILE: {os.environ.get('SSL_CERT_FILE')}\n"
                                 f"env REQUESTS_CA_BUNDLE: {os.environ.get('REQUESTS_CA_BUNDLE')}\n"
                                 f"env CURL_CA_BUNDLE: {os.environ.get('CURL_CA_BUNDLE')}\n"
                                 "Если не помогает — попробуйте удалить переменные окружения SSL_CERT_FILE, REQUESTS_CA_BUNDLE, CURL_CA_BUNDLE и перезапустить Python.\n"
                                 "Если всё равно не работает — попробуйте явно указать системный сертификат Windows через SSL_CERT_FILE.")
            client = genai.Client(api_key=api_key)
        print("[DEBUG] genai.Client создан успешно")
        return client
    except Exception as e:
        print("[ERROR] Ошибка при инициализации клиента:")
        if os.environ.get("GENAI_DEBUG") == "1":
            traceback.print_exc()
        raise

def generate_with_retries(client: genai.Client, model: str, prompt: str) -> str:
    last_exc = None
    for delay in RETRY_DELAYS:
        if delay:
            time.sleep(delay)
        try:
            # Генерация контента (простая форма)
            resp = client.models.generate_content(model=model, contents=prompt)
            # Ответ библиотека возвращает в resp.text (см. доки)
            text = getattr(resp, "text", None)
            if text is None:
                # иногда объект может отличаться — пытаемся безопасно взять str()
                text = str(resp)
            return strip_ansi(text).strip()
        except Exception as e:
            last_exc = e
    raise RuntimeError(f"Generation failed after retries: {last_exc}")

def translate_text(client: genai.Client, model: str, content: str, max_chars: int) -> str:
    chunks = chunk_markdown(content, max_chars)
    translated_chunks: List[str] = []
    total = len(chunks)
    for i, ch in enumerate(chunks, 1):
        print(f"  🔄 chunk {i}/{total} (≈{len(ch)} chars)...")
        prompt = build_prompt(ch)
        out = generate_with_retries(client, model, prompt)
        translated_chunks.append(out)
        print(f"    [DEBUG] Translated chunk output length: {len(out)}")
        print(f"    [DEBUG] Translated chunk (first 100 chars): {out[:100].replace('\\n', ' ')}...")
    return "\n".join(translated_chunks)

def process_file(client: genai.Client, model: str, src: Path, dst: Path, max_chars: int, overwrite: bool):
    if dst.exists() and not overwrite:
        print(f"⏭ skip (exists): {dst}")
        return
    txt = src.read_text(encoding="utf-8", errors="ignore")
    if not txt.strip():
        dst.write_text("", encoding="utf-8")
        print(f"⚠ empty: {src}")
        return
    translated = translate_text(client, model, txt, max_chars)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(translated, encoding="utf-8")
    print(f"✅ saved: {dst}")

# --- Авто-очистка переменных окружения, мешающих certifi ---
for _ssl_env in ["SSL_CERT_FILE", "REQUESTS_CA_BUNDLE", "CURL_CA_BUNDLE"]:
    if os.environ.get(_ssl_env):
        print(f"[INFO] Удаляю переменную окружения {_ssl_env} (мешает работе certifi)")
        del os.environ[_ssl_env]

def walk_and_translate(input_dir: Path, output_dir: Path, model: str, max_chars: int, overwrite: bool, skip_existing: bool):
    print(f"[DEBUG] walk_and_translate: input_dir={input_dir}, output_dir={output_dir}")
    client = init_client(use_vertex=(os.environ.get("GOOGLE_GENAI_USE_VERTEXAI", "False").lower() in ("1","true")))
    print("Client initialized.")
    # Собираем список файлов .md
    files_to_process = []
    for root, _, files in os.walk(input_dir):
        for name in files:
            if name.lower().endswith(".md"):
                src = Path(root) / name
                rel = src.relative_to(input_dir)
                dst = output_dir / rel
                files_to_process.append((src, dst))
    if not files_to_process:
        print(f"[INFO] Нет файлов .md для обработки в {input_dir}")
        return
    print(f"[INFO] Найдено файлов для обработки: {len(files_to_process)}")
    for src, dst in files_to_process:
        print(f"  - {src}")
    for src, dst in files_to_process:
        if skip_existing and dst.exists():
            print(f"⏭ (--skip-existing) {dst}")
            continue
        print(f"Translating: {src}")
        process_file(client, model, src, dst, max_chars, overwrite)

def main():
    ap = argparse.ArgumentParser(description="Translate Markdown directory (RU -> KO) via Google GenAI SDK.")
    ap.add_argument("--input-dir", default="docs/ru", help="Folder with source .md files (default: docs/ru)")
    ap.add_argument("--output-dir", default="docs/ko", help="Where to put translated files (default: docs/ko_translated)")
    ap.add_argument("--model", default=DEFAULT_MODEL, help="Gemini model (default: gemini-2.5-flash)")
    ap.add_argument("--max-chars", type=int, default=DEFAULT_MAX_CHARS, help="Max chars per chunk")
    ap.add_argument("--overwrite", action="store_true", help="Overwrite existing files in output")
    ap.add_argument("--skip-existing", action="store_true", help="Skip files that already exist in output")
    ap.add_argument("--debug", action="store_true", help="Show full traceback on error")
    args = ap.parse_args()

    if args.debug:
        os.environ["GENAI_DEBUG"] = "1"
    else:
        os.environ["GENAI_DEBUG"] = "0"

    inp = Path(args.input_dir).resolve()
    out = Path(args.output_dir).resolve()
    if not inp.exists():
        print(f"Input folder doesn't exist: {inp}")
        return
    out.mkdir(parents=True, exist_ok=True)

    print(f"Using model: {args.model}")
    print(f"Input: {inp}")
    print(f"Output: {out}")
    try:
        walk_and_translate(inp, out, args.model, args.max_chars, args.overwrite, args.skip_existing)
    except Exception as e:
        print("\n[ОШИБКА] Перевод не выполнен:")
        print(f"  {e}")
        if args.debug:
            traceback.print_exc()
        print("\nПроверьте настройки, переменные окружения и наличие certifi.\nЕсли ошибка связана с SSL/certifi — попробуйте: pip install --upgrade certifi\n")

if __name__ == "__main__":
    main()
