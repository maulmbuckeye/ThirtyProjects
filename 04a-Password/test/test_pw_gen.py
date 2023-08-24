import unittest
from pw_gen import password_generator, contains_special, contains_uppercase

class MyTestCase(unittest.TestCase):

    def test_length_one(self):
        self.assertEqual("a", password_generator(1, "a"))

    def test_length_more_than_one(self):
        self.assertEqual("aaaaa", password_generator(5, "a"))

    def test_two_options(self):
        pw = password_generator(512, "ab")
        a_count = pw.count("a")
        b_count = pw.count("b")
        self.assertEqual(512, len(pw), "Checking for right number of characters")
        self.assertGreater(a_count, 0, f"Should have some a's: pwd={pw[:20]}")
        self.assertGreater(b_count, 0, f"Should have some b's: pwd={pw[:20]}")

    def test_contains_uppercase(self):
        self.assertTrue(contains_uppercase("Mike"))

    def test_does_not_contains_uppercase(self):
        self.assertFalse(contains_uppercase("mike"))

    def test_contains_special_character(self):
        self.assertTrue(contains_special("Mike!"))

    def test_does_not_contains_special_character(self):
        self.assertFalse(contains_special("mike"))


if __name__ == '__main__':
    unittest.main()
