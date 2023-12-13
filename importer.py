import pandas as pd
from astroquery.jplhorizons import Horizons

def fetch_object_data(object_id):
    obj = Horizons(id=object_id, id_type='majorbody', location='500@10', epochs={'start':'2023-10-01', 'stop':'2023-10-02', 'step':'1d'})
    eph = obj.ephemerides()
    return eph.to_pandas()

# Список ID объектов: Солнце, планеты и многие из их спутников (но не все)
# Для полного списка вы можете посмотреть документацию JPL HORIZONS или онлайн-версию их сервиса
objects_ids = list(range(1, 40)) + list(range(501, 600)) + list(range(601, 700)) + list(range(701, 800)) + list(range(801, 900)) + list(range(901, 1000))

dataframes = []

for obj_id in objects_ids:
    try:
        df = fetch_object_data(str(obj_id))
        dataframes.append(df)
    except:
        # Некоторые ID могут быть не действительными или отсутствовать в базе данных, поэтому мы пропускаем их
        pass

result = pd.concat(dataframes)
result.to_csv('solar_system_objects_data.csv', index=False)
