from chances import Chances
from words_from_file import Words as RandomWord


class Hangman:
    def __init__(self):
        self.word_to_find = [letter for letter in RandomWord().get_word()]
        self.chances = Chances()
        self.word = ['_' for i in self.word_to_find]

    def get_chances(self):
        return self.chances.get_chances()

    def get_word_to_guess(self) -> str:
        return ' '.join(self.word)

    def guess_letter(self, letter: str) -> None:
        """ self.chances.decrease_chances() raises ChancesError """
        if letter not in self.word_to_find:
            self.chances.decrease_chances()
        self.append_letter(letter)

    def are_all_letters_found(self) -> bool:
        return '_' not in self.word

    def append_letter(self, letter: str) -> None:
        tstart = 0
        for i in range(0, self.word_to_find.count(letter)):
            index = self.word_to_find.index(letter, tstart)
            self.word[index] = letter
            tstart = index + 1

    def is_it_word_to_find(self, word: str) -> bool:
        return word == self.get_word_to_find()

    def get_word_to_find(self) -> str:
        return ''.join(self.word_to_find)
