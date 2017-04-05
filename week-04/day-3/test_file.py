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

    def test_anagram_with_anagram(self):
        mr_test = Apple("test")
        self.assertEqual(mr_test.anagram("tokyo", "kyoto"), True)

    def test_anagram_False_anagram(self):
        mr_test = Apple("test")
        self.assertEqual(mr_test.anagram("ttkyo", "kyoto"), False)




if __name__ == "__main__":
    unittest.main()
