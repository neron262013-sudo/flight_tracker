import pytest
from src.aircraft import Aircraft


def test_aircraft_creation():
    aircraft = Aircraft("Canada", "ABC123", 100, 200)

    assert aircraft.country == "Canada"
    assert aircraft.callsign == "ABC123"
    assert aircraft.velocity == 100
    assert aircraft.altitude == 200


def test_aircraft_validation():
    with pytest.raises(ValueError):
        Aircraft("", "ABC123", 100, 200)

    with pytest.raises(ValueError):
        Aircraft("Canada", "ABC123", -10, 200)

    with pytest.raises(ValueError):
        Aircraft("Canada", "ABC123", 100, -5)


def test_comparison_methods():
    a1 = Aircraft("USA", "A1", 200, 300)
    a2 = Aircraft("USA", "A2", 100, 200)

    assert a1.is_faster_than(a2)
    assert a1.is_higher_than(a2)
