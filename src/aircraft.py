class Aircraft:
    def __init__(self, country: str, callsign: str, velocity: float, altitude: float) -> None:

        # Валидация
        if not isinstance(country, str) or not country:
            raise ValueError("Страна должна быть непустой строкой")

        if not isinstance(callsign, str):
            raise ValueError("Позывной должен быть строкой")

        if velocity < 0:
            raise ValueError("Скорость не может быть отрицательной")

        if altitude < 0:
            raise ValueError("Высота не может быть отрицательной")

        self._country = country
        self._callsign = callsign
        self._velocity = velocity
        self._altitude = altitude

    @property
    def velocity(self):
        return self._velocity

    @property
    def altitude(self):
        return self._altitude

    @property
    def country(self):
        return self._country

    @property
    def callsign(self):
        return self._callsign

    def is_faster_than(self, other) -> bool:
        return self._velocity > other.velocity

    def is_higher_than(self, other) -> bool:
        return self._altitude > other.altitude

    def __str__(self):
        return f"{self._callsign}, {self._country}, speed={self._velocity}, altitude={self._altitude}"
