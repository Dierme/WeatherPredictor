# The script is supposed to be run by daemon to collect the weather data for the city

from ApiClient import ApiClient
from config import CONFIG
from Database import DataBase
from models.City import City
from models.Weather import Weather
from utils import unix_to_datetime
import json

db = DataBase()
db.generate()


def request_weather(city):
    apiClienet = ApiClient(CONFIG['appid'], city.city_id)
    response = apiClienet.weather()
    response = json.loads(response.text)

    # Save weather to DB if entry for this time does not exist
    if len(Weather.get_by_unix(response['dt'])) == 0:
        weather_entry = Weather.save(city_id=city.city_id,
                           desc=response['weather'][0]['main'],
                           temp_max=response['main']['temp_max'],
                           temp_min=response['main']['temp_min'],
                           pressure=response['main']['pressure'],
                           humidity=response['main']['humidity'],
                           visibility=response['visibility'],
                           wind_speed=response['wind']['speed'],
                           dt=response['dt'])
        print("Entry for time {} added successfully".format(unix_to_datetime(weather_entry.dt)))
        return weather_entry
    print("Entry was not added, because it already exists for time {}".format(unix_to_datetime(response['dt'])))
    return None


if __name__ == '__main__':
    city = City.get_by_name('Stockholm')
    request_weather(city)