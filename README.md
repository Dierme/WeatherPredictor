# WeatherPredictor
Collect data using OpenWeatherMap and try to predict weather for specified time

Short description:
The idea is to collect weather data from OpenWeatherMap, store it locally (as bulk history download is not free)
and use it to predict weather. This can in be interesting in several ways: 
1. Determine which classifier performs best.
2. See how accuratly can we predict data for both short and long term.
3. Understanding and finding features can improve predictions

Project structure:
get_weather.py should be run by daemon to collect data from api
main.py tries to predict data based on current entries in DB
ApiClient.py - implementation of client, used for communication with api
Database.py - implementation of DB class, based on pony.orm
models/ - model representation of tables in DB

Setup:
Create new virtual environment
Run: pip install -r req.txt
Set up daemon to run get_weathet.py
