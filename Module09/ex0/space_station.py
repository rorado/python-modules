
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)
    userName: str = Field(min_length=3, max_length=20, default="admin")


def print_station(station: SpaceStation) -> None:
    status = "Operational" if station.is_operational else "Not operational"
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Status: {status}")
    print(f"userName: {station.userName}")


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    valid_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2026-03-21T10:30:00",
        notes="Primary low-earth orbit research station.",
    )
    print_station(valid_station)

    print("=" * 40)
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="ISS002",
            name="Outpost Alpha",
            crew_size=30,
            power_level=71.0,
            oxygen_level=88.0,
            last_maintenance=datetime.now(),
        )
    except ValidationError as error:
        first_error = error.errors()[0]
        print(first_error["msg"])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
