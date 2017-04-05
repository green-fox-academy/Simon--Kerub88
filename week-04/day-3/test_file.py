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

    def test_string_to_dic(self):
        mr_test = Apple("test")
        self.assertEqual(mr_test.string_to_dictionary("tokyo"), {"t": 1, "o": 2, "k": 1, "y": 1})

    def test_string_to_dic(self):
        mr_test = Apple("test")
        self.assertEqual(mr_test.string_to_dictionary("000"), {"0": 3})


    def test_fibonacci_method_zero(self):
        fibo = Apple("test")
        self.assertEqual(fibo.fibonacci(0), 0)

    def test_fibonacci_method_one(self):
        fibo = Apple("test")
        self.assertEqual(fibo.fibonacci(1), 1)

    def test_fibonacci_method_number(self):
        fibo = Apple("test")
        self.assertEqual(fibo.fibonacci(6), 8)

if __name__ == "__main__":
    unittest.main()
