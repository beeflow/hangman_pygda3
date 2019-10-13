from random import randint
import os


class Words:
    def get_path(self):
        return os.path.abspath(os.path.dirname(__file__))

    def get_word(self):
        lines = 0
        with open(f'{self.get_path()}/words.txt') as file:
            while file.readline():
                lines += 1

        random_line = randint(1, lines)

        word = None
        with open(f'{self.get_path()}/words.txt') as file:
            for i in range(random_line):
                word = file.readline().strip()

        return word


if __name__ == '__main__':
    word = Words()
    print(word.get_word())
