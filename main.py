# The script tries to predict the weather based on collected data

from Database import DataBase
from models.Weather import Weather
from sklearn.linear_model import LinearRegression
from utils import unix_to_datetime
import numpy as np

db = DataBase()
db.generate()

if __name__ == '__main__':

    all_w = Weather.get_all()
    time_X = []
    temperature_Y = []
    for w in all_w:
        time_X.append([w.dt])
        temperature_Y.append(w.temp_min)

    prediction_time = 1519819000 # unix

    model = LinearRegression()
    model.fit(time_X, temperature_Y)
    sample = np.array([prediction_time]).reshape(1, -1)
    predicted_temp = model.predict(sample)[0]
    print('Program thinks, that at {} the temp will be {:.3}'.format(
        unix_to_datetime(prediction_time),
        predicted_temp
    ))


