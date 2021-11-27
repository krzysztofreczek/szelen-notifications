import data


def analyze_trainings(trainings: [data.TrainingData], user: str) -> str:
    count = 0
    for training in trainings:
        if user == training.user:
            count = count + 1

    return "You have " + str(count) + " training(s)"

