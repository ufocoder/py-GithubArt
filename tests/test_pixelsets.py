import pytest
import importlib

from github_art.pixelsets import LettersPixelSet


def normalize(pixel_set, heigth):
    rows = [[] for _ in range(heigth)]
    for letter in pixel_set:
        for i in range(heigth):
            rows[i] = rows[i] + letter[i]
    return rows


@pytest.mark.parametrize('dictionary', ['alphanumeric', 'alphanumeric2x'])
def test_one_letter_pixelset(dictionary):
    letters = importlib.import_module('github_art.dictionaries.' + dictionary)
    pixel_set = LettersPixelSet('a', dictionary)
    pixels = pixel_set.get_pixel_set()
    assert letters.a == pixels


@pytest.mark.parametrize('dictionary', ['alphanumeric', 'alphanumeric2x'])
def test_two_letter_pixelset(dictionary):
    letters = importlib.import_module('github_art.dictionaries.' + dictionary)
    pixelset = LettersPixelSet('ab', dictionary)
    pixels_from_pixelset = pixelset.get_pixel_set()
    letters_set = (letters.a, letters.space, letters.b)
    pixels_from_letters = normalize(letters_set, letters.HEIGHT)
    assert pixels_from_pixelset == pixels_from_letters


if __name__ == '__main__':
    pytest.main()