import unittest
from MyWebChecker import get_websites
from unittest.mock import patch, mock_open


class MyTestsForGetWebsites(unittest.TestCase):
    ONE_LINE_FILE = """1,"https://apple.com"
"""

    TWO_LINE_FILE = ONE_LINE_FILE + """2,"https://facebook.com"""""

    WITHOUT_HTTPS_FILE = """1,"apple.com",
2,"facebook.com"
"""

    def test_problem_with_file(self):
        self.assertEqual([], get_websites("foobar.csv"))

    def test_empty_file(self):
        with self.patch_open_with_mock(""):
            self.assertEqual([], get_websites("foobar.csv"))

    @staticmethod
    def patch_open_with_mock(read_data):
        return patch('MyWebChecker.open', mock_open(read_data=read_data))

    def test_one_line(self):
        with self.patch_open_with_mock(self.ONE_LINE_FILE):
            self.assertEqual(["https://apple.com"], get_websites("foobar.csv"))

    def test_two_line(self):
        with self.patch_open_with_mock(self.TWO_LINE_FILE):
            self.assertEqual(["https://apple.com", "https://facebook.com"], get_websites("foobar.csv"))

    def test_without_https(self):
        with self.patch_open_with_mock(self.WITHOUT_HTTPS_FILE):
            self.assertEqual(["https://apple.com", "https://facebook.com"], get_websites("foobar.csv"))

class MyTestsForGetWebsites(unittest.TestCase):

if __name__ == '__main__':
    unittest.main()
