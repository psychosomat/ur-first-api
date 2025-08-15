from fastapi import FastAPI, HTTPException, Response, status, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator
from typing import List
import random
from fastapi.middleware.cors import CORSMiddleware

class Spaceship(BaseModel):
    """
    Technical passport (model) of a spaceship.
    """
    id: int
    name: str = Field(..., min_length=3, max_length=50, description="Ship's name")
    type: str
    launch_year: int = Field(..., gt=1950, description="Launch year must be after 1950")
    status: str

class SpaceshipCreate(BaseModel):
    """Model for creating a new ship (without ID)."""
    name: str = Field(..., min_length=3, max_length=50)
    type: str
    launch_year: int = Field(..., gt=1950)
    status: str

    @validator('name')
    def name_must_not_be_forbidden(cls, v):
        """Checks that the ship's name is not on the forbidden list."""
        if 'Death Star' in v:
            raise ValueError('Names like "Death Star" are forbidden by Imperial decree!')
        return v.title() # Also capitalize the name

db_spaceships = {
    1: {
        "id": 1,
        "name": "Voyager-1",
        "type": "Probe",
        "launch_year": 1977,
        "status": "Active"
    },
    2: {
        "id": 2,
        "name": "Hubble Space Telescope",
        "type": "Telescope",
        "launch_year": 1990,
        "status": "Active"
    },
    3: {
        "id": 3,
        "name": "ISS",
        "type": "Station",
        "launch_year": 1998,
        "status": "In orbit"
    }
}

app = FastAPI(
    title="Fleet Management API",
    description="API for managing a fleet of spacecraft.",
    version="1.0.0",
)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:5500",
    "null"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    """
    This is the Mission Control Center message that everyone
    who connects to the main gateway sees.
    """
    return {"message": "Welcome to the Space Fleet Mission Control Center!"}

@app.get("/spaceships", response_model=List[Spaceship], tags=["Spacecraft"])
def get_spaceships():
    """
    Returns a list of ships. Each item in the list
    is validated against the Spaceship model.
    """
    return list(db_spaceships.values())

@app.get("/spaceships/{ship_id}", response_model=Spaceship, tags=["Spacecraft"])
def get_spaceship(ship_id: int):
    """
    Returns data about a ship, corresponding to the Spaceship model.
    """
    ship = db_spaceships.get(ship_id)
    return ship

@app.post("/spaceships", response_model=Spaceship, status_code=201, tags=["Spacecraft"])
def create_spaceship(ship: SpaceshipCreate):
    """
    Adds a new spacecraft to the registry.
    """
    new_id = max(db_spaceships.keys() or [0]) + 1
    new_ship = Spaceship(id=new_id, **ship.dict())
    db_spaceships[new_id] = new_ship.dict()
    return new_ship

@app.put("/spaceships/{ship_id}", response_model=Spaceship)
def update_spaceship(ship_id: int, ship_update: SpaceshipCreate):
    """
    Completely updates the data about a spacecraft.
    """
    if ship_id not in db_spaceships:
        raise HTTPException(status_code=404, detail="Spacecraft not found")

    updated_ship = Spaceship(id=ship_id, **ship_update.dict())
    db_spaceships[ship_id] = updated_ship.dict()

    return updated_ship

@app.delete("/spaceships/{ship_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_spaceship(ship_id: int):
    """
    Removes a spacecraft from the registry.
    """
    if ship_id not in db_spaceships:
        raise HTTPException(status_code=404, detail="Spacecraft not found")

    del db_spaceships[ship_id]

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.exception_handler(ValueError)
async def value_error_exception_handler(request: Request, exc: ValueError):
    """
    Global handler for all ValueError exceptions,
    to return a standardized JSON.
    """
    return JSONResponse(
        status_code=400,
        content={"message": f"Data error: {str(exc)}"},
    )
