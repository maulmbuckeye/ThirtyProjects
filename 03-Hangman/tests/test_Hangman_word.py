import unittest
from HangmanWord import HangmanWord


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.foo_word = HangmanWord("foo")
        self.sphinix_word = HangmanWord("sphinix")

    def test_len_of_word_to_guess(self):
        self.assertEqual(len(self.foo_word), 3)

    def test_letter_in_word(self):
        self.assertTrue(self.foo_word.is_letter_in("f"))

    def test_letter_not_in_word(self):
        self.assertFalse(self.foo_word.is_letter_in("x"))

    def test_show_nothing_if_no_guess(self):
        self.assertEqual(str(self.foo_word), "___")

    def test_guesses_with_no_guesses(self):
        self.assertEqual(set(), self.foo_word.guesses())

    def test_guesses_with_a_incorrect_guess(self):
        self.foo_word.is_letter_in("x")
        self.assertSetEqual({"x"}, self.foo_word.guesses())

    def test_guesses_with_a_correct_and_incorrect_guess(self):
        self.foo_word.is_letter_in("f")
        self.foo_word.is_letter_in("z")
        self.assertSetEqual({"z", "f"}, self.foo_word.guesses())

    def test_show_something_if_letter_is_correct(self):
        self.foo_word.is_letter_in("f")
        self.assertEqual("f__", str(self.foo_word))

    def test_show_something_if_some_are_correct_and_others_not(self):
        self.sphinix_word.is_letter_in("s")
        self.sphinix_word.is_letter_in("t")
        self.sphinix_word.is_letter_in("i")
        self.assertEqual("s__i_i_", str(self.sphinix_word))


if __name__ == '__main__':
    unittest.main(verbosity=1)
