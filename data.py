from datetime import date


class Training:
    user: str
    date: date

    def __init__(self, u: str, d: date):
        self.user = u
        self.date = d
