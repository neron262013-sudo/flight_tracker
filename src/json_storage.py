import json

from src.aircraft import Aircraft
from src.storage_base import StorageBase


class JsonStorage(StorageBase):
    """
    Класс для хранения информации о самолётах в JSON-файле.
    Реализует методы добавления, получения и удаления
    данных о самолётах.
    """

    # где будем хранить файл
    def __init__(self, filename: str = "data/aircrafts.json") -> None:
        self.filename = filename

    def _read_file(self) -> list[dict]:
        """
        Считывает данные из JSON-файла.
        Если файл отсутствует или пуст,
        возвращается пустой список.
        """
        try:
            with open(self.filename, "r", encoding="utf-8") as file:

                # Удаляем лишние пробелы и переносы строк.
                content = file.read().strip()

                if not content:
                    return []

                return json.loads(content)

        except FileNotFoundError:
            return []

    def _write_file(self, data: list[dict]) -> None:
        """
        Записывает список самолётов в JSON-файл.
        """
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_aircraft(self, aircraft: Aircraft) -> None:
        """
        Добавляет самолёт в хранилище.
        """
        data = self._read_file()

        data.append(
            {
                "country": aircraft.country,
                "callsign": aircraft.callsign,
                "velocity": aircraft.velocity,
                "altitude": aircraft.altitude,
            }
        )

        self._write_file(data)

    def get_aircrafts(self, **filters) -> list[Aircraft]:
        """
        Получает самолёты по указанным критериям.
        """
        data = self._read_file()
        result = []

        # Проверяем каждый самолёт на соответствие фильтрам.
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
        """
        Удаляет самолёт из хранилища по его позывному.
        """
        data = self._read_file()

        # Оставляем только те записи,
        # чей позывной не совпадает с удаляемым самолётом.
        data = [item for item in data if item.get("callsign") != aircraft.callsign]

        self._write_file(data)
