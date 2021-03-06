import unittest
import leap_year

class TestLeapYear(unittest.TestCase):
    #Test to make sure multiples of 4 are leap years
    def test_leap_year1(self):
        self.assertEqual(True, leap_year.leap_year(2020))

    #Test to ensure years divisible by 100 are not leap years
    def test_leap_year2(self):
        self.assertEqual(False, leap_year.leap_year(2100))

    def test_leap_year3(self):
        self.assertEqual(True, leap_year.leap_year(2000))


if __name__ == "__main__":
    unittest.main()
        