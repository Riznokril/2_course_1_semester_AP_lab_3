import unittest
from hamster import Hamster

class TestHamster(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(Hamster.find_max_number_of_hamsters("hamster_in_test_1.txt"), 2)

    def test_case_2(self):
        self.assertEqual(Hamster.find_max_number_of_hamsters("hamster_in_test_2.txt"), 3)

if __name__ == '__main__':
    unittest.main()
