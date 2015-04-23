import string
import unittest

from github_art import letters, letters2x


class LettersTestCase(unittest.TestCase):
    def setUp(self):
        self.dictionaries = [
            letters,
            letters2x
        ]

    def test_alphabet_letters(self):
        for dictionary in self.dictionaries:
            for character in string.lowercase:
                self.assertTrue(getattr(dictionary, character))

    def test_height_exists(self):
        for dictionary in self.dictionaries:
            for character in string.lowercase:
                self.assertTrue(getattr(dictionary, 'HEIGHT'))

    def test_space_letter(self):
        for dictionary in self.dictionaries:
            for character in string.lowercase:
                self.assertTrue(getattr(dictionary, 'space'))


if __name__ == '__main__':
    unittest.main()