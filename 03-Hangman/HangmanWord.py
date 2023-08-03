class HangmanWord:
    def __init__(self, word_to_guess):
        self.word_to_guess = word_to_guess
        self.guessed_letters = set()

    def __len__(self):
        return len(self.word_to_guess)

    def is_letter_in(self, lettercanidate):
        self.guessed_letters.add(lettercanidate)
        return lettercanidate in self.word_to_guess

    def __str__(self):
        return ''.join([ l if l in self.guessed_letters else '_' for l in self.word_to_guess])

    def guesses(self):
        return self.guessed_letters


if __name__ == "__main__":
    HangmanWord("foobar")
