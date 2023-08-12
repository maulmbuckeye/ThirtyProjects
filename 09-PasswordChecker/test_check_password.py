import unittest
from unittest.mock import patch, mock_open
from my_solution import check_password


class MyTestCase(unittest.TestCase):

    def test_an_okay_password(self):
        self.assertTrue(check_password("ok_password"))

    def test_password_is_not_okay(self):
        self.assertFalse(check_password("password"))

    def test_passwd_is_not_okay(self):
        self.assertFalse(check_password("passwd"))

    def test_mike_ulm_is_not_okay(self):
        with patch("my_solution.open",
                   side_effect=FileNotFoundError):
            self.assertFalse(check_password("mike_ulm"))

    def test_if_no_file(self):
        with patch("my_solution.open",
                   side_effect=FileNotFoundError):
            self.assertFalse(check_password("password"))


if __name__ == '__main__':
    unittest.main()
