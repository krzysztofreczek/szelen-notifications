import data
from datetime import date


def analyze_trainings(trainings: [data.TrainingData], user: str, last_monday_date: date) -> str:
    count = 0
    for training in trainings:
        training_date_in_string_format = training.date
        training_date_in_date_format = date.fromisoformat(training_date_in_string_format)

        if user == training.user and last_monday_date <= training_date_in_date_format:
            count = count + 1

    return "You have " + str(count) + " training(s) this week"

