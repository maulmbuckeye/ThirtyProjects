from secrets import choice
import string


def password_generator(length: int, characters: str):
    return "".join([choice(characters) for _ in range(length)])


def contains_uppercase(a_string: str):
    return contains(a_string, string.ascii_uppercase)


def contains_special(a_string: str):
    return contains(a_string, string.punctuation)


def contains(a_string: str, to_be_contained : str):
    for character in a_string:
        if character in to_be_contained:
            return True
    return False
