from chances import ChancesError
from hangman import Hangman


class HangmanGame:
    __messagess = {
        'pl': {
            'chances_left': 'Pozostało szans',
            'give_a_letter': 'Podaj literę lub słowo',
            'lose': 'Słabiaku!!!!!',
            'win': 'Gratulacje!!!',
            'word_info': 'Szukane słowo to'
        }
    }
    def __init__(self, language='pl'):
        self.hangman = Hangman()
        self.language = language

    def translate(self, key):
        return self.__messagess[self.language][key]

    def play(self):
        while True:
            print(f"{self.translate('chances_left')}: {self.hangman.get_chances()}")
            print(self.hangman.get_word_to_guess())
            letter = input('Podaj literę lub słowo: ')

            if self.hangman.is_it_word_to_find(letter):
                self.win()
                break

            try:
                self.hangman.guess_letter(letter)
            except ChancesError:
                self.lose()
                break

            if self.hangman.are_all_letters_found():
                self.win()
                break

    def lose(self):
        print('\nSłabiaku!!!!!')
        self.print_word_to_find()

    def win(self):
        print('\nGratulacje!!!')
        self.print_word_to_find()

    def print_word_to_find(self):
        print(f'Szukane słowo to: {self.hangman.get_word_to_find()}')


def main_game():
    while True:
        game = HangmanGame()
        game.play()

        if input('Chcesz grać ponownie? [t/n]: ') == 'n':
            break


if __name__ == '__main__':
    main_game()
