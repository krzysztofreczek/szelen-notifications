class Trainings:
    data = []

    def __init__(self, trainings):
        Trainings.data = trainings


class TrainingData:
    user = ""
    timestamp = ""

    def __init__(self, user, timestamp):
        TrainingData.user = user
        TrainingData.timestamp = timestamp
