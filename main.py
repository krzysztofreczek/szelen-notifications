import data

# Miro: https://miro.com/app/board/o9J_lhf0WP8=/
if __name__ == '__main__':
    print("Hello World!")

    training1 = data.TrainingData('Ania', '2021-11-21')
    training2 = data.TrainingData('Ania', '2021-11-22')
    training3 = data.TrainingData('Krzysio', '2021-11-20')
    training4 = data.TrainingData('Krzysio', '2021-11-21')

    trainings = data.Trainings([training1, training2, training3, training4])

    print(trainings)
