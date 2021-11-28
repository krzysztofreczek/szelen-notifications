class TrainingData:
    user: str
    timestamp: str

    def __init__(self, user: str, timestamp: str):
        self.user = user
        self.timestamp = timestamp
