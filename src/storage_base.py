from abc import ABC, abstractmethod

from src.aircraft import Aircraft


class StorageBase(ABC):

    @abstractmethod
    def add_aircraft(self, aircraft: Aircraft) -> None:
        """Добавить самолет в хранилище"""
        pass

    @abstractmethod
    def get_aircrafts(self, **filters) -> list[Aircraft]:
        """Получить самолеты по критериям"""
        pass

    @abstractmethod
    def delete_aircraft(self, aircraft: Aircraft) -> None:
        """Удалить самолет"""
        pass
