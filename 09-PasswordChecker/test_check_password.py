import unittest
from unittest.mock import patch, mock_open
from my_solution import password_check, PasswordResult

FILE_BEING_TESTED = "my_solution.open"


class TestPasswordResult(unittest.TestCase):
    def test_password(self):
        result = PasswordResult(True, password='foo')
        self.assertEqual("foo", result.password)

    def test_password_only_set_via_constructor(self):
        dummy = PasswordResult(True)
        with self.assertRaises(AttributeError):
            dummy.password = 'mike'

    def test_string_of_good_password(self):
        result = str(PasswordResult(True))
        self.assertEqual("✅", result)

    def test_string_of_good_password_with_password(self):
        result = str(PasswordResult(True, password="good_password"))
        self.assertEqual("good_password: ✅", result)

    def test_string_of_bad_password(self):
        result = str(PasswordResult(False))
        self.assertEqual("❌", result)

    def test_string_of_common_password_rank(self):
        result = str(PasswordResult(False, rank=3))
        self.assertEqual("❌ (#3)", result)



class MyUnitTests(unittest.TestCase):

    COMMON_PASSWORDS = """silly
mike_ulm
another
password"""

    def password_check_with_mock_file(self, candidate_password) -> PasswordResult:
        with patch(FILE_BEING_TESTED, mock_open(read_data=self.COMMON_PASSWORDS)):
            return password_check(candidate_password)

    def test_passwd_is_not_okay(self):
        result = self.password_check_with_mock_file("password")
        self.assertFalse(result)
        self.assertEqual(4, result.rank)
        self.assertEqual("Commonly used password", result.msg)

    def test_ting_is_okay_with_mock(self):
        result = self.password_check_with_mock_file("ting")
        self.assertTrue(result)

    def password_check_with_no_file_found(self, candidate_password: str) -> PasswordResult:
        with patch(FILE_BEING_TESTED, side_effect=FileNotFoundError):
            return password_check(candidate_password)

    def test_if_no_file(self):
        result = self.password_check_with_no_file_found("password")
        self.assertFalse(result)
        self.assertEqual(1, result.rank)
        self.assertEqual("Commonly used password", result.msg)

    def test_for_something_not_on_internal_list(self):
        """ Checks that 'ting' is not in no-file-found list."""
        result = self.password_check_with_no_file_found("another")
        self.assertTrue(result)


class MyIntegrationTests(unittest.TestCase):
    def test_int_password_is_not_okay(self):
        result = password_check("password")
        self.assertFalse(result)
        self.assertEqual(2, result.rank)
        self.assertEqual("Commonly used password", result.msg)

    def test_int_an_okay_password(self):
        self.assertTrue(password_check("ok_password"))

    def test_int_if_no_file(self):
        result = password_check("password",
                                list_of_bad="does_not_exist.txt")
        self.assertFalse(result)
        self.assertEqual(1, result.rank)
        self.assertEqual("password: ❌ (#1)", str(result))


if __name__ == '__main__':
    unittest.main()
