import unittest
from work_file import Apple

class TestApple(unittest.TestCase):

    def test_get_apple(self):
        redapple = Apple("red")
        self.assertEqual(redapple.get_apple(), "redapple")


    def test_sum(self):
        self.assertEqual(sum([1,9]), 10)

    def test_sum_for_zero(self):
        self.assertEqual(sum([]), 0)





if __name__ == "__main__":
    unittest.main()
