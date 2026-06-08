from abc import ABC, abstractmethod


class ApiBase(ABC):
    @abstractmethod
    def get_data(self, *args, **kwargs):
        """Получение данных из API."""
        pass
