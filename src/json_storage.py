import json
from src.storage_base import StorageBase
from src.aircraft import Aircraft


class JsonStorage(StorageBase):

    def __init__(self, filename: str = "data/aircrafts.json") -> None:
        self.filename = filename

    def _read_file(self) -> list[dict]:
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _write_file(self, data: list[dict]) -> None:
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_aircraft(self, aircraft: Aircraft) -> None:
        data = self._read_file()

        data.append({
            "country": aircraft.country,
            "callsign": aircraft.callsign,
            "velocity": aircraft.velocity,
            "altitude": aircraft.altitude,
        })

        self._write_file(data)

    def get_aircrafts(self, **filters) -> list[Aircraft]:
        data = self._read_file()
        result = []

        for item in data:
            match = True

            for key, value in filters.items():
                if item.get(key) != value:
                    match = False
                    break

            if match:
                result.append(Aircraft(**item))

        return result

    def delete_aircraft(self, aircraft: Aircraft) -> None:
        data = self._read_file()

        data = [
            item for item in data
            if item.get("callsign") != aircraft.callsign
        ]

        self._write_file(data)
