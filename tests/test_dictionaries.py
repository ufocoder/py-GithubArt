import string
import pytest

from github_art.dictionaries import alphanumeric, alphanumeric2x


@pytest.mark.parametrize('dictionary', [alphanumeric, alphanumeric2x])
def test_alphabet_letters(dictionary):
    for character in string.lowercase:
        assert dictionary.characters.get(character)

@pytest.mark.parametrize('dictionary', [alphanumeric, alphanumeric2x])
def test_numeric_letters(dictionary):
    for number in range(0, 9):
        assert not dictionary.characters.get(str(number)) is None

@pytest.mark.parametrize('dictionary', [alphanumeric, alphanumeric2x])
def test_height_exists(dictionary):
    assert getattr(dictionary, 'HEIGHT')


@pytest.mark.parametrize('dictionary', [alphanumeric, alphanumeric2x])
def test_space_letter(dictionary):
    assert getattr(dictionary, 'space')


if __name__ == '__main__':
    pytest.main()