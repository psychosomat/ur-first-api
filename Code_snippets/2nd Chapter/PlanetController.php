<?php

namespace App\Http\Controllers;

use App\Http\Requests\StorePlanetRequest;
use App\Http\Requests\UpdatePlanetRequest;
use App\Models\Planet;
use Illuminate\Http\Request;
use App\Exceptions\CannotDeleteEarthException;

class PlanetController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index(Request $request)
    {
        $planets = Planet::paginate($request->get('per_page', 15));
    	return response()->json($planets);
    }

    public function random(Request $request)
    {
        $planet = Planet::inRandomOrder()->first();
        return response()->json($planet);
    }

    /**
     * Store a newly created resource in storage.
     */
	public function store(StorePlanetRequest $request)
	{
		$validated = $request->validated();
		$planet = Planet::create($validated);
		return response()->json($planet, 201);
	}

    /**
     * Display the specified resource.
     */
    public function show(Planet $planet)
    {
        return response()->json($planet);
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(UpdatePlanetRequest $request, Planet $planet)
    {
		$validated = $request->validated();
		$planet->update($validated);
		return response()->json($planet);
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Planet $planet)
    {
		if (strtolower($planet->name) === 'earth') {
			throw new CannotDeleteEarthException('The destruction of planet Earth is prohibited by the Galactic Code.');
		}
        $planet->delete();
    	return response()->json(null, 204); // No Content
    }
}
