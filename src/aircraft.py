class Aircraft:
    """
    Класс, описывающий самолёт и его характеристики.

    Хранит основную информацию о самолёте:
    - страна регистрации
    - позывной
    - скорость полёта
    - высота полёта

    Поддерживает:
    - инкапсуляцию данных
    - сравнение самолётов по скорости и высоте
    """

    def __init__(self, country: str, callsign: str, velocity: float, altitude: float) -> None:

        # Проверка входных данных перед созданием объекта.
        if not isinstance(country, str) or not country:
            raise ValueError("Страна должна быть непустой строкой")

        if not isinstance(callsign, str):
            raise ValueError("Позывной должен быть строкой")

        if velocity < 0:
            raise ValueError("Скорость не может быть отрицательной")

        if altitude < 0:
            raise ValueError("Высота не может быть отрицательной")

        # Сохранение данных в закрытые атрибуты объекта.
        # Использование префикса "_" означает, что атрибуты
        # не должны изменяться напрямую извне класса.
        # Доступ к ним осуществляется через свойства (@property),
        self._country = country
        self._callsign = callsign
        self._velocity = velocity
        self._altitude = altitude

    # Свойства (properties) предоставляют безопасный доступ
    # к закрытым атрибутам класса.
    # Благодаря этому код снаружи объекта может получать значения:
    # aircraft.velocity
    # aircraft.altitude
    # aircraft.country
    # aircraft.callsign
    # не обращаясь напрямую к _velocity, _altitude и т.д.
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
        """
        Проверяет, быстрее ли текущий самолёт другого.
        """
        return self._velocity > other.velocity

    def is_higher_than(self, other) -> bool:
        """
        Проверяет, выше ли текущий самолёт другого.
        """
        return self._altitude > other.altitude

    def __str__(self):
        return f"{self._callsign}, {self._country}, speed={self._velocity}, altitude={self._altitude}"
