from .chances_error import ChancesError


class Chances:
    def __init__(self, chances=9):
        self.chances = chances

    def get_chances(self):
        return self.chances

    def decrease_chances(self):
        self.chances -= 1

        if self.chances == 0:
            raise ChancesError('Nie masz już szans :P')
