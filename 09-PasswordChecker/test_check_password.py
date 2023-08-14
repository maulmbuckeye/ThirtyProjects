import unittest
from unittest.mock import patch, mock_open
from my_solution import password_check


class MyUnitTests(unittest.TestCase):

    def test_password_is_first_on_internal_list(self):
        """ Checks that 'ting' is not in no-file-found list."""
        with patch("my_solution.open",
                   side_effect=FileNotFoundError):
            self.assertEqual((False, '1'), password_check("password"))

    def test_passwd_is_not_okay(self):
        self.assertFalse(password_check("passwd")[0])

    def test_ting_is_okay_if_no_file(self):
        """ Checks that 'ting' is not in no-file-found list."""
        with patch("my_solution.open",
                   side_effect=FileNotFoundError):
            self.assertEqual((True, ''), password_check("ting"))

    def test_mike_ulm_is_not_okay_if_no_file(self):
        with patch("my_solution.open",
                   side_effect=FileNotFoundError):
            self.assertEqual((False, '3'), password_check("mike_ulm"))

    def test_if_no_file(self):
        with patch("my_solution.open",
                   side_effect=FileNotFoundError):
            self.assertEqual((False, "1"), password_check("password"))


class MyIntegrationTests(unittest.TestCase):
    def test_password_is_not_okay(self):
        self.assertEqual((False, '2'), password_check("password"))

    def test_an_okay_password(self):
        self.assertEqual((True, ''), password_check("ok_password"))

    def test_if_no_file(self):
        result = password_check("password",
                                list_of_bad="does_not_exist.txt")
        self.assertEqual((False, "1"), result)


if __name__ == '__main__':
    unittest.main()
