from astroquery.jplsbdb import SBDB
import pandas as pd

# Установка базы данных SBDB
sbdb = SBDB()

# Получение списка небесных тел с радиусом больше 1 км
query = sbdb.query('SELECT * FROM sbdb WHERE radius > 1')
data = query.table

# Сохранение данных в CSV-файл
data.to_csv('solar_system_objects.csv', index=False)

print("Данные о небесных телах с радиусом больше 1 км сохранены в solar_system_objects.csv")
