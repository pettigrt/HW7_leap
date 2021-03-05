import unittest
import leap_year

class TestLeapYear(unittest.TestCase):
    def test_leap_year1(self):
        self.assertEqual(True, leap_year.leap_year(2020))


if __name__ == "__main__":
    unittest.main()
        