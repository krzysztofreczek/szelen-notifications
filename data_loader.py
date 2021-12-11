import data
import http.client
import json


def load_data() -> [data.TrainingData]:
    conn = http.client.HTTPSConnection("raw.githubusercontent.com")
    conn.request("GET", "/krzysztofreczek/szelen/master/db/events.0.js", '', {})
    res = conn.getresponse()
    data_string = res.read().decode("utf-8")
    data_string = data_string[30:]
    data_string = data_string.replace('date', '"date"')
    data_string = data_string.replace('user', '"user"')

    data_json = json.loads(data_string)
    trainings = []

    for d in data_json:
        if 'user' in d:
            user = d['user']
            date = d['date']
            training = data.TrainingData(user, date)
            trainings.append(training)

    return trainings
