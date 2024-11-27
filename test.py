import unittest
from program_1 import count_word, sort_words, word_count_sort

class TestWordFrequency(unittest.TestCase):

    def test_count_word(self):
        # Test case 1: Normal input
        line = "which is better python 2 or python 3"
        expected = {'which': 1, 'is': 1, 'better': 1, 'python': 2, '2': 1, 'or': 1, '3': 1}
        result = count_word(line)
        self.assertEqual(result, expected)

        # Test case 2: Edge case with empty string
        line = ""
        expected = {}
        result = count_word(line)
        self.assertEqual(result, expected)


    def test_sort_words(self):
        # Test case 1: Normal input
        word_counts = {'which': 1, 'is': 1, 'better': 1, 'python': 2, '2': 1, 'or': 1, '3': 1}
        expected = [('2', 1), ('3', 1), ('better', 1), ('is', 1), ('or', 1), ('python', 2), ('which', 1)]
        result = sort_words(word_counts)
        self.assertEqual(result, expected)

        # Test case 2: Edge case with no words
        word_counts = {}
        expected = []
        result = sort_words(word_counts)
        self.assertEqual(result, expected)


    def test_word_count_sort(self):
        # Test case 1: Normal input
        line = "which is better python 2 or python 3"
        expected = [('2', 1), ('3', 1), ('better', 1), ('is', 1), ('or', 1), ('python', 2), ('which', 1)]
        result = word_count_sort(line)
        self.assertEqual(result, expected)

        # Test case 2: Edge case with an empty string
        line = ""
        expected = []
        result = word_count_sort(line)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
