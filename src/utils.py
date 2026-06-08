def normalize_value(value):
    """
    Приводит значение к числу и нормализует его.

    Правила:
    - None → 0
    - преобразует значение в float
    - отрицательные значения заменяет на 0

    Используется для очистки данных,
    полученных из внешнего API (OpenSky).
    """
    if value is None:
        return 0
    value = float(value)
    return max(value, 0)
