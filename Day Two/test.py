from typing import Dict, List
import unittest
from assignment import AssignmentTwo

class TestCases(unittest.TestCase):
    #Question 1
    def test_is_power_of_four(self):
        self.assertTrue(AssignmentTwo.is_power_of_four(64), None)

    #Question 2 Test
    def test_is_perfect_square(self):
        self.assertTrue(AssignmentTwo.is_perfect_square(4), None)
        self.assertFalse(AssignmentTwo.is_perfect_square(3), None)

    #Question 3 Test
    def test_guess_number(self):
        pass

    #Question 4 Test
    def test_web_request(self):
        pass

    #Question 5
    def test_timeout_request(self):
        pass

    #Question 6
    def test_basic_stat(self):
        self.assertEqual(AssignmentTwo.basic_stat([59, 69, 45, 83, 55, 10]), {'mean': 53.5, 'mode': 59, 'variance': 621.5, 'median': 57.0})



if __name__ == '__main__':
    unittest.main()