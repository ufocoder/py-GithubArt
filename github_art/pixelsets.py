import letters
import letters2x


class PixetSet(object):
    def get_pixel_set(self):
        pass


class LettersPixelSet(PixetSet):
    def __init__(self, string, size=None):
        self.__letters = self.__load_letters(size)
        self.__pixel_set = self.__form_pixel_set(string)
        self.__pixel_set = self.__normalize_pixel_set(self.__pixel_set)

    def get_pixel_set(self):
        return self.__pixel_set

    def __load_letters(self, size=None):
        size = int(size) or 1
        if size == 2:
            return letters2x
        else:
            return letters

    def __form_pixel_set(self, string):
        pixel_set = ()
        space_pixel_set = self.__get_space_pixel_set()
        for letter in string:
            pixel_set = pixel_set + (space_pixel_set, self.__get_letter_position(letter), )

        return pixel_set

    def __normalize_pixel_set(self, pixel_set):
        rows = [[] for _ in range(self.__letters.HEIGHT)]
        for letter in pixel_set:
            for i in range(self.__letters.HEIGHT):
                rows[i] = rows[i] + letter[i]

        return rows

    def __get_space_pixel_set(self):
        try:
            return getattr(self.__letters, 'space')
        except AttributeError:
            raise SystemExit('Space letter is not exists')

    def __get_letter_position(self, letter):
        try:
            return getattr(self.__letters, letter)
        except AttributeError:
            raise SystemExit('Letter ' + letter + ' is not exists')
