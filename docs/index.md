# Welcome

<div style="display:flex;gap:8px;flex-wrap:wrap;">
    <!-- English -->
    <button onclick="switchLang('en')" style="display:inline-flex;align-items:center;gap:6px;padding:6px 10px;border:none;border-radius:6px;background:#7e56c2;color:#fff;font-size:14px;cursor:pointer;">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="14" viewBox="0 0 60 30">
            <clipPath id="clip-en">
                <path d="M0,0 v30 h60 v-30 z"/>
            </clipPath>
            <g clip-path="url(#clip-en)">
                <path d="M0,0 v30 h60 v-30 z" fill="#012169"/>
                <path d="M0,0 L60,30 M60,0 L0,30" stroke="#fff" stroke-width="6"/>
                <path d="M0,0 L60,30 M60,0 L0,30" stroke="#C8102E" stroke-width="4"/>
                <path d="M30,0 v30 M0,15 h60" stroke="#fff" stroke-width="10"/>
                <path d="M30,0 v30 M0,15 h60" stroke="#C8102E" stroke-width="6"/>
            </g>
        </svg>
        English
    </button>
	<!-- Korean -->
    <button onclick="switchLang('ko')" style="display: inline-flex; align-items: center; gap: 6px; padding: 6px 10px; border: none; background: #7e56c2; color: white; border-radius: 6px; cursor: pointer;">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="14" viewBox="0 0 30 20">
            <rect width="30" height="20" fill="#fff"/>
            <circle cx="15" cy="10" r="6" fill="#C60C30"/>
            <path d="M15 4a6 6 0 0 1 0 12" fill="#003478"/>
            <g stroke="#000" stroke-width="1">
                <path d="M3,3 l3,3 M3,5 l3,3 M3,7 l3,3"/>
                <path d="M24,3 l3,3 M24,5 l3,3 M24,7 l3,3"/>
                <path d="M3,13 l3,3 M3,15 l3,3"/>
                <path d="M24,13 l3,3 M24,15 l3,3"/>
            </g>
        </svg>
        한국어
    </button>
    <!-- Russian -->
    <button onclick="switchLang('ru')" style="display:inline-flex;align-items:center;gap:6px;padding:6px 10px;border:none;border-radius:6px;background:#7e56c2;color:#fff;font-size:14px;cursor:pointer;">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="14" viewBox="0 0 9 6">
            <rect width="9" height="3" y="0" fill="#fff"/>
            <rect width="9" height="2" y="2" fill="#0039a6"/>
            <rect width="9" height="1" y="4" fill="#d52b1e"/>
        </svg>
        Русский
    </button>
    <!-- Spanish -->
    <button onclick="switchLang('es')" style="display:inline-flex;align-items:center;gap:6px;padding:6px 10px;border:none;border-radius:6px;background:#7e56c2;color:#fff;font-size:14px;cursor:pointer;">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="14" viewBox="0 0 9 6">
            <rect width="9" height="6" fill="#aa151b"/>
            <rect width="9" height="2" y="2" fill="#f1bf00"/>
        </svg>
        Español
    </button>
    <!-- Portuguese -->
    <button onclick="switchLang('pt')" style="display:inline-flex;align-items:center;gap:6px;padding:6px 10px;border:none;border-radius:6px;background:#7e56c2;color:#fff;font-size:14px;cursor:pointer;">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="14" viewBox="0 0 720 504">
            <rect width="720" height="504" fill="#006600"/>
            <polygon points="360,84 84,252 360,420 636,252" fill="#ffcc00"/>
            <circle cx="360" cy="252" r="84" fill="#002776"/>
        </svg>
        Português
    </button>
    <!-- Chinese (Simplified) -->
    <button onclick="switchLang('zh')" style="display:inline-flex;align-items:center;gap:6px;padding:6px 10px;border:none;border-radius:6px;background:#7e56c2;color:#fff;font-size:14px;cursor:pointer;">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="14" viewBox="0 0 30 20">
            <rect width="30" height="20" fill="#de2910"/>
            <polygon fill="#ffde00" points="5,2 6,5 9,5 6.5,7 7.5,10 5,8.5 2.5,10 3.5,7 1,5 4,5"/>
            <polygon fill="#ffde00" points="10,2 10.5,3 11.5,3 10.7,3.6 11,4.5 10,4 9,4.5 9.3,3.6 8.5,3 9.5,3"/>
            <polygon fill="#ffde00" points="11,4 11.5,5 12.5,5 11.7,5.6 12,6.5 11,6 10,6.5 10.3,5.6 9.5,5 10.5,5"/>
            <polygon fill="#ffde00" points="11,6 11.5,7 12.5,7 11.7,7.6 12,8.5 11,8 10,8.5 10.3,7.6 9.5,7 10.5,7"/>
            <polygon fill="#ffde00" points="10,8 10.5,9 11.5,9 10.7,9.6 11,10.5 10,10 9,10.5 9.3,9.6 8.5,9 9.5,9"/>
        </svg>
        中文
    </button>
    <!-- French -->
    <button onclick="switchLang('fr')" style="display:inline-flex;align-items:center;gap:6px;padding:6px 10px;border:none;border-radius:6px;background:#7e56c2;color:#fff;font-size:14px;cursor:pointer;">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="14" viewBox="0 0 3 2">
            <rect width="1" height="2" x="0" fill="#0055a4"/>
            <rect width="1" height="2" x="1" fill="#fff"/>
            <rect width="1" height="2" x="2" fill="#ef4135"/>
        </svg>
        Français
    </button>
</div>

<div id="description-en">
    <h2><b>Welcome aboard, cadet! 🚀</b></h2>
    <p>This guide is your first step into the boundless universe of APIs. It doesn't claim to be a perfect encyclopedia, but serves as a practical guide to help you quickly grasp the basics and start creating your own projects. Here you will find real-world examples, clear explanations, and a pinch of cosmic inspiration.</p>
    <p>This tutorial is intended for beginners, students, and junior developers (up to mid-level). If you notice an error or want to suggest improvements—both for the material and the translation—I would be happy to receive your feedback.</p>
    <p><i>The translation from English was done with the help of AI and may contain inaccuracies.</i></p>
    <a href="en/Chapter%201%20-%20API%20Basics/1/">🚀 Go to the tutorial</a>
    <hr>
    <h2>☄ Support the mission</h2>
    <p>Creating this tutorial is a long and complex flight that requires a lot of time and energy. If you found the material useful, you can help refuel our expedition's tanks. Every contribution is another orbit towards new useful materials.</p>
    <a href='https://ko-fi.com/K3K41JFJ32' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi4.png?v=6' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
</div>

<div id="description-ru" style="display:none;">
    <h2><b>Добро пожаловать на борт, курсант! 🚀</b></h2>
    <p>Это пособие — ваш первый шаг в безграничную вселенную API. Оно не претендует на звание идеальной энциклопедии, но служит практичным путеводителем, который поможет быстро понять основы и начать создавать свои проекты. Здесь вы найдёте реальные примеры, понятные объяснения и щепотку космического вдохновения.</p>
    <p>Учебник рассчитан на новичков, студентов и джунов (максимум до уровня миддл). Если вы заметите ошибку или захотите предложить улучшения — как по материалу, так и по переводу — буду рад вашей обратной связи.</p>
    <p><i>Перевод с английского выполнен при помощи ИИ и может содержать неточности.</i></p>
    <a href="/ru/Глава%201%20-%20Основы%20API/1/">🚀 Перейти к учебнику</a>
    <hr>
    <h2>☄ Поддержите миссию</h2>
    <p>Создание этого учебника — долгий и сложный полёт, который требует немало времени и энергии. Если материал оказался для вас полезным, вы можете помочь пополнить топливные баки нашей экспедиции.
    Каждая поддержка — ещё один шаг к новым материалам.</p>
    <a href='https://ko-fi.com/K3K41JFJ32' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi4.png?v=6' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
</div>

<div id="description-es" style="display:none;">
    <h2><b>¡Bienvenido a bordo, cadete! 🚀</b></h2>
    <p>Este manual es tu primer paso en el universo ilimitado de las API. No pretende ser una enciclopedia perfecta, pero sirve como una guía práctica que te ayudará a comprender rápidamente los conceptos básicos y comenzar a crear tus propios proyectos. Aquí encontrarás ejemplos reales, explicaciones claras y una pizca de inspiración cósmica.</p>
    <p>El tutorial está dirigido a principiantes, estudiantes y desarrolladores junior (como máximo, de nivel medio). Si notas un error o quieres sugerir mejoras, tanto en el material como en la traducción, estaré encantado de recibir tus comentarios.</p>
    <p><i>La traducción del inglés se realizó con la ayuda de IA y puede contener imprecisiones.</i></p>
    <a href="/es/Capítulo%201%20Fundamentos%20de%20la%20API/1/">🚀 Ir al tutorial</a>
    <hr>
    <h2>☄ Apoya la misión</h2>
    <p>Crear este tutorial es un vuelo largo y complejo que requiere mucho tiempo y energía. Si el material te ha resultado útil, puedes ayudar a rellenar los tanques de combustible de nuestra expedición. Cada apoyo es una órbita más hacia nuevos materiales útiles.</p>
    <a href='https://ko-fi.com/K3K41JFJ32' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi4.png?v=6' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
</div>

<div id="description-pt" style="display:none;">
    <h2><b>Bem-vindo a bordo, cadete! 🚀</b></h2>
    <p>Este manual é o seu primeiro passo no universo ilimitado das APIs. Não pretende ser uma enciclopédia perfeita, mas serve como um guia prático que o ajudará a compreender rapidamente os conceitos básicos e a começar a criar os seus próprios projetos. Aqui encontrará exemplos reais, explicações claras e uma pitada de inspiração cósmica.</p>
    <p>O tutorial destina-se a iniciantes, estudantes e programadores júnior (no máximo, de nível intermediário). Se notar algum erro ou quiser sugerir melhorias — tanto no material como na tradução — terei todo o gosto em receber o seu feedback.</p>
    <p><i>A tradução do inglês foi feita com a ajuda de IA e pode conter imprecisões.</i></p>
    <a href="/pt/Capítulo%201%20-%20Noções%20básicas%20da%20API/1/">🚀 Ir para o tutorial</a>
    <hr>
    <h2>☄ Apoie a missão</h2>
    <p>Criar este tutorial é um voo longo e complexo que requer muito tempo e energia. Se o material lhe foi útil, pode ajudar a abastecer a expedição. Cada apoio é mais uma órbita em direção a novos materiais úteis.</p>
    <a href='https://ko-fi.com/K3K41JFJ32' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi4.png?v=6' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
</div>

<div id="description-zh" style="display:none;">
    <h2><b>欢迎登船，学员！🚀</b></h2>
    <p>本手册是您进入无限API世界的第一步。它并非一本完美的百科全书，而是一本实用的指南，可帮助您快速掌握基础知识并开始创建自己的项目。在这里，您会发现真实的示例、清晰的解释和一丝宇宙的灵感。</p>
    <p>本教程面向初学者、学生和初级开发人员（最多为中级）。如果您发现错误或希望提出改进建议——无论是针对材料还是翻译——我将很高兴收到您的反馈。</p>
    <p><i>该译文是在人工智能的帮助下从英文翻译而来，可能存在不准确之处。</i></p>
    <a href="/zh/第1章 - API基础/1/">🚀 前往教程</a>
    <hr>
    <h2>☄ 支持任务</h2>
    <p>创建本教程是一项漫长而复杂的飞行，需要大量的时间和精力。如果您觉得这些材料有用，可以帮助我们为探险队的油箱加满油。每一次支持都是向着新的有用材料的又一圈轨道。</p>
    <a href='https://ko-fi.com/K3K41JFJ32' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi4.png?v=6' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
</div>

<div id="description-ko" style="display:none;">
    <h2><b>탑승을 환영합니다, 생도! 🚀</b></h2>
    <p>이 핸드북은 무한한 API의 세계로 나아가는 첫 걸음입니다. 완벽한 백과사전은 아니지만, 기본 사항을 빠르게 파악하고 자신만의 프로젝트를 시작하는 데 도움이 되는 실용적인 가이드 역할을 합니다. 여기에서는 실제 예제, 명확한 설명, 그리고 약간의 우주적 영감을 찾을 수 있습니다.</p>
    <p>이 튜토리얼은 초보자, 학생, 주니어 개발자(초급 및 주니어 개발자 대상)를 대상으로 합니다. 자료나 번역에 대한 오류를 발견하거나 개선 사항을 제안하고 싶다면 언제든지 피드백을 보내주세요.</p>
    <p><i>영어 번역은 AI의 도움을 받아 이루어졌으며 부정확한 내용이 포함될 수 있습니다.</i></p>
    <a href="ko/제1장%20-%20API의%20기본%20개념/1/">🚀 튜토리얼로 이동</a>
    <hr>
    <h2>☄ 임무 지원</h2>
    <p>이 튜토리얼을 만드는 것은 많은 시간과 에너지가 필요한 길고 복잡한 비행입니다. 자료가 유용했다면 탐험대의 연료 탱크를 보충하는 데 도움을 줄 수 있습니다. 모든 지원은 새로운 유용한 자료를 향한 또 다른 궤도입니다.</p>
    <a href='https://ko-fi.com/K3K41JFJ32' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi4.png?v=6' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
</div>

<div id="description-fr" style="display:none;">
    <h2><b>Bienvenue à bord, cadet ! 🚀</b></h2>
    <p>Ce manuel est votre premier pas dans l'univers infini des API. Il ne prétend pas être une encyclopédie parfaite, mais sert de guide pratique pour vous aider à comprendre rapidement les bases et à commencer à créer vos propres projets. Vous y trouverez des exemples concrets, des explications claires et une pincée d'inspiration cosmique.</p>
    <p>Ce tutoriel s'adresse aux débutants, aux étudiants et aux développeurs juniors (au plus, de niveau intermédiaire). Si vous remarquez une erreur ou si vous souhaitez suggérer des améliorations, tant pour le matériel que pour la traduction, je serai heureux de recevoir vos commentaires.</p>
    <p><i>La traduction de l'anglais a été réalisée à l'aide de l'IA et peut contenir des inexactitudes.</i></p>
    <a href="/fr/Chapitre%201%20-%20Bases%20de%20l'API/1/">🚀 Aller au tutoriel</a>
    <hr>
    <h2>☄ Soutenez la mission</h2>
    <p>La création de ce tutoriel est un vol long et complexe qui demande beaucoup de temps et d'énergie. Si le matériel vous a été utile, vous pouvez aider à remplir les réservoirs de carburant de notre expédition. Chaque soutien est une autre orbite vers de nouveaux matériaux utiles.</p>
    <a href='https://ko-fi.com/K3K41JFJ32' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi4.png?v=6' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
</div>

<script>
function switchLang(lang) {
    document.getElementById('description-en').style.display = 'none';
    document.getElementById('description-ru').style.display = 'none';
    document.getElementById('description-es').style.display = 'none';
    document.getElementById('description-pt').style.display = 'none';
    document.getElementById('description-zh').style.display = 'none';
    document.getElementById('description-ko').style.display = 'none';
    document.getElementById('description-fr').style.display = 'none';
    document.getElementById('description-' + lang).style.display = 'block';
}
</script>
