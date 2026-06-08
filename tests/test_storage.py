import os
import tempfile

from src.aircraft import Aircraft
from src.json_storage import JsonStorage


def test_add_and_get_aircraft():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        storage = JsonStorage(tmp.name)

        aircraft = Aircraft("USA", "ABC123", 100, 200)
        storage.add_aircraft(aircraft)

        result = storage.get_aircrafts(callsign="ABC123")

        assert len(result) == 1
        assert result[0].callsign == "ABC123"

    os.remove(tmp.name)


def test_delete_aircraft():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        storage = JsonStorage(tmp.name)

        aircraft = Aircraft("USA", "ABC123", 100, 200)
        storage.add_aircraft(aircraft)

        storage.delete_aircraft(aircraft)

        result = storage.get_aircrafts(callsign="ABC123")

        assert len(result) == 0

    os.remove(tmp.name)
