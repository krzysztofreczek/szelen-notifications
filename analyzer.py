import data
from datetime import date


def analyze_trainings(trainings: [data.Training], user: str, last_monday_date: date) -> str:
    count = 0
    for t in trainings:
        if user == t.user and last_monday_date <= t.date:
            count = count + 1

    return "You have " + str(count) + " training(s) this week"

