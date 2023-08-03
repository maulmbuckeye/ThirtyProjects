from HangmanWord import HangmanWord


def the_game():
    player_name = input("What is your name? ")
    print(f"Welcome to hangman, {player_name}!")
    failed_tries: int = 3
    print(f"You will be given {failed_tries} tries.")
    word = HangmanWord("pizza")
    while not word.is_done() and failed_tries > 0:
        print("Word: ", word)
        guessed_letter = input("Enter a letter: ")
        if not word.is_letter_in(guessed_letter):
            failed_tries -= 1
            print(f"Wrong. You have {failed_tries} left")
    print("Word: ", word.secret_word())

if __name__ == "__main__":
    the_game()
