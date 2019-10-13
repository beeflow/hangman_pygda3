from random import randint


class RandomWord:
    """Klasa do losowania wyrazów"""
    def __init__(self):
        self.words = ('test', 'testtest')

    def get_word(self) -> str:
        index = randint(0, len(self.words) - 1)
        return self.words[index]
