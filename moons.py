import csv
from astroquery.jplhorizons import Horizons

def fetch_planets_and_moons():
    # Список идентификаторов планет Солнечной системы
    planet_ids = ['199', '299', '399', '499', '599', '699', '799', '899', '999']

    celestial_bodies = []

    for planet_id in planet_ids:
        # Получаем информацию о планете
        planet = Horizons(id=planet_id, id_type='majorbody')
        celestial_bodies.append(planet.ephemerides()[0]['targetname'])

        # Получаем информацию о спутниках планеты
        moons = Horizons.moons(planet_id)
        if moons is not None:
            for moon in moons:
                celestial_bodies.append(moon['name'])

    return celestial_bodies

def main():
    celestial_bodies = fetch_planets_and_moons()

    # Сохраняем данные в CSV файл
    with open('solar_system_bodies.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for body in celestial_bodies:
            writer.writerow([body])

if __name__ == "__main__":
    main()
