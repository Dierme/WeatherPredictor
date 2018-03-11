# The script tries to predict the weather based on collected data

from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction import DictVectorizer
from Database import DataBase
from models.Weather import Weather
from sklearn.linear_model import LinearRegression

db = DataBase()
db.generate()

if __name__ == '__main__':

    all_w = Weather.get_all()
    X = []
    Y = []
    for w in all_w:
        X.append({
            'desc': w.description,
            'pressure': w.pressure,
            'humidity': w.humidity,
            'visibility': w.visibility,
            'wind_speed': w.wind_speed,
            'month': w.month
        })
        Y.append(w.temp_min)

    print(X[0])
    print(Y[0])

    pipeline = make_pipeline(
        DictVectorizer(),
        LinearRegression(normalize=True)
    )

    pipeline.fit(X, Y)

    sample0 = {
            'desc': 'Clouds',
            'pressure': 1030,
            'humidity': 80,
            'visibility': 3000,
            'wind_speed': 3.5,
            'month': 2
    }

    sample1 = {
        'desc': 'Snow',
        'pressure': 1046,
        'humidity': 84,
        'visibility': 2003,
        'wind_speed': 3.5,
        'month': 2
    }

    predicted_temp = pipeline.predict(sample1)
    print('Program thinks, the temp will be {:.3}'.format(predicted_temp[0]))


    # X = np.array([20, 22, 25, 27, 30, 31, 31, 34, 42, 50])
    # Y = np.array([10000, 12000, 16000, 20000, 30000, 33000, 34000, 38000, 49000, 60000])
    # pipeline.fit(X[:, np.newaxis], Y[:, np.newaxis])
    # print(pipeline)