<?php

use App\Http\Middleware\HandleAppearance;
use App\Http\Middleware\HandleInertiaRequests;
use Illuminate\Foundation\Application;
use Illuminate\Foundation\Configuration\Exceptions;
use Illuminate\Foundation\Configuration\Middleware;
use Illuminate\Http\Middleware\AddLinkHeadersForPreloadedAssets;
use Illuminate\Http\Request;
use Illuminate\Database\Eloquent\ModelNotFoundException;
use Symfony\Component\HttpKernel\Exception\NotFoundHttpException;
use App\Exceptions\CannotDeleteEarthException;

return Application::configure(basePath: dirname(__DIR__))
    ->withRouting(
        web: __DIR__.'/../routes/web.php',
        api: __DIR__.'/../routes/api.php',
        commands: __DIR__.'/../routes/console.php',
        health: '/up',
    )
    ->withMiddleware(function (Middleware $middleware) {
        $middleware->encryptCookies(except: ['appearance', 'sidebar_state']);

        $middleware->web(append: [
            HandleAppearance::class,
            HandleInertiaRequests::class,
            AddLinkHeadersForPreloadedAssets::class,
        ]);
    })
    ->withExceptions(function (Exceptions $exceptions) {
		$exceptions->render(function (CannotDeleteEarthException $e, Request $request) {
			return response()->json([
				'message' => 'Operation prohibited.',
				'details' => $e->getMessage()
			], 403);
		});

		$exceptions->render(function (ModelNotFoundException $e, Request $request) {
			if ($request->is('api/*')) {
				return response()->json([
					'message' => 'The requested resource was not found in our galaxy..'
				], 404);
			}
		});

		$exceptions->render(function (NotFoundHttpException $e, Request $request) {
			if ($request->is('api/*')) {
				return response()->json([
					'message' => 'There is no such space route...'
				], 404);
			}
		});

		$exceptions->render(function (Throwable $e, Request $request) {
			if ($request->is('api/*')) {
				$message = config('app.debug')
					? 'An error has occurred: ' . $e->getMessage()
					: 'An unexpected error has occurred on board. Engineers have already been called.';

				return response()->json(['message' => $message], 500);
			}
		});
    })->create();
