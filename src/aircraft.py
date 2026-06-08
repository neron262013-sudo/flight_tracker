class Aircraft:
    def __init__(
            self,
            country: str,
            callsign: str,
            velocity: float,
            altitude: float) -> None:

        # Валидация
        if not isinstance(country, str) or not country:
            raise ValueError("Страна должна быть непустой строкой")

        if not isinstance(callsign, str):
            raise ValueError("Позывной должен быть строкой")

        if velocity < 0:
            raise ValueError("Скорость не может быть отрицательной")

        if altitude < 0:
            raise ValueError("Высота не может быть отрицательной")

        self.country = country
        self.callsign = callsign
        self.velocity = velocity
        self.altitude = altitude

    def is_faster_than(self, other) -> bool:
        return self.velocity > other.velocity

    def is_higher_than(self, other) -> bool:
        return self.altitude > other.altitude
