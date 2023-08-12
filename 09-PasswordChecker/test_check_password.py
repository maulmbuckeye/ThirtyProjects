import unittest
from my_solution import check_password


class MyTestCase(unittest.TestCase):

    def test_an_okay_password(self):
        self.assertTrue(check_password("ok_password"))

    def test_password_is_not_okay(self):
        self.assertFalse(check_password("password"))

    def test_passwd_is_not_okay(self):
        self.assertFalse(check_password("passwd"))


if __name__ == '__main__':
    unittest.main()
