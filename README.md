# WeatherPredictor
Collect data using OpenWeatherMap and try to predict weather for specified time

Short description:
The idea is to collect weather data from OpenWeatherMap, store it locally (as bulk history download is not free)
and use it to predict weather. This can in be interesting in several ways: 
1. Determine which classifier performs best.
2. See how accuratly can we predict data for both short and long term.
3. Understanding and finding features can improve predictions

Project structure:
1. get_weather.py should be run by daemon to collect data from api
2. main.py tries to predict data based on current entries in DB
3. ApiClient.py - implementation of client, used for communication with api
4. Database.py - implementation of DB class, based on pony.orm
5. models/ - model representation of tables in DB

Setup:
1. Create new virtual environment
2.Run: pip install -r req.txt
3.Set up daemon to run get_weathet.py
