from pony.orm import *
from Database import DataBase

db = DataBase.get_database()


class City(db.Entity):
    id = PrimaryKey(int, auto=True)
    city_id = Required(int)
    name = Required(str)
    weather = Set("Weather")

    # ---- Query
    @staticmethod
    @db_session
    def get_all():
        return select(p for p in City)[:]

    @staticmethod
    @db_session
    def get_by_id(city_id):
        city = select(c for c in City if c.city_id == city_id)[:][0]
        return city

    @staticmethod
    @db_session
    def get_by_name(name):
        city = select(c for c in City if c.name == name)[:][0]
        return city

    @staticmethod
    @db_session
    def create_city(name, city_id):
        city = City(name=name, city_id=city_id)
        return city