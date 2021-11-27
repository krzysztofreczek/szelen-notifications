from unittest import TestCase
import analyzer
import data


class Test(TestCase):
    def test_no_trainings_provided(self):
        user = "Ania"
        trainings = []
        message = analyzer.analyze_trainings(trainings, user)
        self.assertEqual("You have 0 training(s)", message)

    def test_few_trainings_provided_for_the_user(self):
        user = "Ania"
        trainings = [
            data.TrainingData("Ania", "2021-11-20"),
            data.TrainingData("Ania", "2021-11-22"),
        ]
        message = analyzer.analyze_trainings(trainings, user)
        self.assertEqual("You have 2 training(s)", message)

    def test_few_trainings_provided_for_another_user(self):
        user = "Ania"
        trainings = [
            data.TrainingData("Krzysio", "2021-11-20"),
            data.TrainingData("Krzysio", "2021-11-22"),
            data.TrainingData("Ania", "2021-11-22"),
        ]
        message = analyzer.analyze_trainings(trainings, user)
        self.assertEqual("You have 1 training(s)", message)
