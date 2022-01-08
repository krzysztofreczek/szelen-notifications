from unittest import TestCase
import analyzer
import data
from datetime import date

user = "Ania"
last_monday_date = date.fromisoformat("2021-11-22")


class Test(TestCase):
    def test_no_trainings_provided(self):
        trainings = []
        message = analyzer.analyze_trainings(trainings, user, last_monday_date)
        self.assertEqual("You have 0 training(s) this week", message)

    def test_few_trainings_provided_for_the_user(self):
        trainings = [
            data.Training("Ania", date.fromisoformat("2021-11-20")),
            data.Training("Ania", date.fromisoformat("2021-11-22")),
            data.Training("Ania", date.fromisoformat("2021-11-24")),
        ]
        message = analyzer.analyze_trainings(trainings, user, last_monday_date)
        self.assertEqual("You have 2 training(s) this week", message)

    def test_few_trainings_provided_for_another_user(self):
        trainings = [
            data.Training("Krzysio", date.fromisoformat("2021-11-20")),
            data.Training("Krzysio", date.fromisoformat("2021-11-22")),
            data.Training("Ania", date.fromisoformat("2021-11-22")),
        ]
        message = analyzer.analyze_trainings(trainings, user, last_monday_date)
        self.assertEqual("You have 1 training(s) this week", message)
