from pony.orm import *
from Database import DataBase
from models.City import City
import utils

db = DataBase.get_database()


class Weather(db.Entity):
    id = PrimaryKey(int, auto=True)
    city = Required("City")
    description = Required(str)
    temp_max = Required(float)
    temp_min = Required(float)
    pressure = Required(float)
    humidity = Required(float)
    visibility = Required(float)
    wind_speed = Required(float)
    month = Required(int)
    dt = Required(int)              # unix

    # ---- Query
    @staticmethod
    @db_session
    def get_all():
        return select(entry for entry in Weather)[:]

    @staticmethod
    @db_session
    def get_by_unix(unix):
        return select(entry for entry in Weather if entry.dt == unix)[:]

    @staticmethod
    @db_session
    def get_all():
        all_w = select(w for w in Weather)[:]
        return all_w

    @staticmethod
    @db_session
    def save(city_id, desc, temp_max, temp_min, pressure, humidity, visibility, wind_speed, dt):
        city = City.get_by_id(city_id)
        entry = Weather(city=city,
                        description=desc,
                        temp_max=temp_max,
                        temp_min=temp_min,
                        pressure=pressure,
                        humidity=humidity,
                        visibility=visibility,
                        wind_speed=wind_speed,
                        month=utils.get_month_by_dt(dt),
                        dt=dt)
        return entry

