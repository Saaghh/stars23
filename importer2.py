import csv
from astroquery.jplhorizons import Horizons
from tqdm import tqdm

def fetch_objects(object_list):
    results = []

    for obj_id in tqdm(object_list, desc="Fetching data"):
        try:
            obj = Horizons(id=obj_id, location='500@10', epochs={'start': '2023-01-01', 'stop': '2023-01-02', 'step': '1d'}, id_type=None)
            eph = obj.ephemerides()
            results.append({
                "Name": eph['targetname'][0],
                "Radius (km)": eph['radius'][0],
                "Type": eph['type'][0]
            })
        except ValueError:
            # Для Солнца и других подобных объектов получим физические свойства
            obj = Horizons(id=obj_id, location='500@10', id_type=None)
            info = obj.ephemerides(quantities='9')  # Код 9 относится к радиусу
            results.append({
                "Name": info['targetname'][0],
                "Radius (km)": info['radiuss'][0],  # Обратите внимание на двойную 's' в 'radiuss'
                "Type": "Star" if obj_id == "Sun" else "Unknown"
            })

    return results

if __name__ == "__main__":
    object_ids = ['Sun', 'Mercury', 'Venus', 'Earth', 'Moon', 'Mars', 'Phobos', 'Deimos', 'Jupiter', 'Io', 'Europa', 'Ganymede', 'Callisto', 
                  'Saturn', 'Mimas', 'Enceladus', 'Tethys', 'Dione', 'Rhea', 'Titan', 'Hyperion', 'Iapetus', 'Uranus', 'Miranda', 'Ariel', 
                  'Umbriel', 'Titania', 'Oberon', 'Neptune', 'Triton', 'Pluto', 'Charon']

    data = fetch_objects(object_ids)

    with open('solar_system_bodies.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["Name", "Radius (km)", "Type"])
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    print("Data saved to solar_system_bodies.csv")
