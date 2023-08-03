import unittest
from HangmanWord import HangmanWord


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.foo = HangmanWord("foo")
        self.sphinx = HangmanWord("sphinx")

    def test_len_of_word_to_guess(self):
        self.assertEqual(len(self.foo), 3)

    def test_letter_in_word(self):
        self.assertTrue(self.foo.is_letter_in("f"))

    def test_letter_not_in_word(self):
        self.assertFalse(self.foo.is_letter_in("x"))

    def test_show_nothing_if_no_guess(self):
        self.assertEqual(str(self.foo), "___")

    def test_guesses_with_no_guesses(self):
        self.assertEqual(set(), self.foo.guesses())

    def test_guesses_with_a_incorrect_guess(self):
        self.foo.is_letter_in("x")
        self.assertSetEqual({"x"}, self.foo.guesses())

    def test_guesses_with_a_correct_and_incorrect_guess(self):
        self.foo.is_letter_in("f")
        self.foo.is_letter_in("z")
        self.assertSetEqual({"z", "f"}, self.foo.guesses())

    def test_show_something_if_letter_is_correct(self):
        self.foo.is_letter_in("f")
        self.assertEqual("f__", str(self.foo))

    def test_show_something_if_some_are_correct_and_others_not(self):
        self.sphinx.is_letter_in("s")
        self.sphinx.is_letter_in("t")
        self.sphinx.is_letter_in("i")
        self.assertEqual("s__i__", str(self.sphinx))

    def test_not_done_at_start(self):
        self.assertFalse(self.foo.is_done())

    def test_is_done_true(self):
        self.foo.is_letter_in("f")
        self.foo.is_letter_in("o")
        self.assertTrue(self.foo.is_done())

    def test_secret_word(self):
        self.assertEqual("foo", self.foo.secret_word())


if __name__ == '__main__':
    unittest.main(verbosity=1)
