from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_safety_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        has_leadership = any(
            member.rank in {Rank.COMMANDER, Rank.CAPTAIN}
            for member in self.crew
        )
        if not has_leadership:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
                )

        if self.duration_days > 365:
            experienced_count = sum(
                member.years_experience >= 5
                for member in self.crew
            )
            if experienced_count < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (> 365 days) require at least 50% "
                    "experienced crew (5+ years)"
                )

        if any(not member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def print_mission(mission: SpaceMission) -> None:
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) "
            f"- {member.specialization}"
        )


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 41)

    valid_mission = SpaceMission(
        mission_id="M2026_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2027-01-15T06:00:00",
        duration_days=900,
        crew=[
            {
                "member_id": "C01",
                "name": "Sarah Connor",
                "rank": "commander",
                "age": 42,
                "specialization": "Mission Command",
                "years_experience": 16,
                "is_active": True,
            },
            {
                "member_id": "C02",
                "name": "John Smith",
                "rank": "lieutenant",
                "age": 34,
                "specialization": "Navigation",
                "years_experience": 7,
                "is_active": True,
            },
            {
                "member_id": "C03",
                "name": "Alice Johnson",
                "rank": "officer",
                "age": 29,
                "specialization": "Engineering",
                "years_experience": 6,
                "is_active": True,
            },
        ],
        budget_millions=2500.0,
    )
    print_mission(valid_mission)

    print("=" * 41)
    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="M2026_TEST",
            mission_name="Deep Space Survey",
            destination="Europa",
            launch_date=datetime.now(),
            duration_days=120,
            crew=[
                {
                    "member_id": "X01",
                    "name": "Lena Park",
                    "rank": "officer",
                    "age": 31,
                    "specialization": "Science",
                    "years_experience": 8,
                    "is_active": True,
                },
                {
                    "member_id": "X02",
                    "name": "Noah Reed",
                    "rank": "lieutenant",
                    "age": 33,
                    "specialization": "Operations",
                    "years_experience": 9,
                    "is_active": True,
                },
            ],
            budget_millions=600.0,
        )
    except ValidationError as error:
        first_error = error.errors()[0]
        print(first_error["msg"])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
