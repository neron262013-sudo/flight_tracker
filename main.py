from src.api_adapter import APIAdapter
from src.json_storage import JsonStorage
from src.aircraft import Aircraft
from src.utils import normalize_value

def main():
    api = APIAdapter()
    storage = JsonStorage()

    country = input("Введите страну: ")

    # получаем самолёты из API
    api.get_aeroplanes(country)

    # сохраняем в storage
    for plane in api.aeroplanes.get("states", []):
        aircraft = Aircraft(
            country=country,
            callsign=plane[1],
            velocity=normalize_value(plane[9]),
            altitude=normalize_value(plane[7]),
        )

        storage.add_aircraft(aircraft)


    # топ N по высоте
    n = int(input("Введите топ N по высоте: "))

    all_planes = storage.get_aircrafts()

    top_by_altitude = sorted(
        all_planes,
        key=lambda x: x.altitude,
        reverse=True
    )[:n]

    print("\nТоп по высоте:")
    for plane in top_by_altitude:
        print(plane)

    # Фильтр по стране
    filter_country = input("\nВведите страну для фильтра: ")

    filtered = storage.get_aircrafts(country=filter_country)

    print("\nСамолёты по стране:")
    for plane in filtered:
        print(plane)


if __name__ == "__main__":
    main()
