from skyfield.api import load
import csv

def write_to_csv(celestial_bodies):
    with open('celestial_bodies.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for body in celestial_bodies:
            writer.writerow([body])

def fetch_celestial_bodies():
    ts = load.timescale()
    eph = load('de421.bsp')
    # Извлечем имена планет и их спутников из файла ephemeris
    bodies = []
    for idx, name in enumerate(eph.names()):
        try:
            decoded_name = name.split(b'  ')[1].decode('utf-8')
            bodies.append(decoded_name)
        except:
            pass
    return bodies

if __name__ == "__main__":
    celestial_bodies = fetch_celestial_bodies()
    write_to_csv(celestial_bodies)
