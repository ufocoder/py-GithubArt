import importlib


class PixetSet(object):
    def get_pixel_set(self):
        pass


class LettersPixelSet(PixetSet):
    def __init__(self, string, dictionary):
        self.__dictionary = self.__load_dictionary(dictionary)
        self.__pixel_set = self.__form_pixel_set(str(string).lower())
        self.__pixel_set = self.__normalize_pixel_set(self.__pixel_set)

    def get_pixel_set(self):
        return self.__pixel_set

    def __load_dictionary(self, dictionary):
        return importlib.import_module('github_art.dictionaries.' + dictionary)

    def __form_pixel_set(self, string):
        pixel_set = ()
        space_pixel_set = self.__get_space_pixel_set()

        for index, character in enumerate(string):
            pixel_set = pixel_set + (space_pixel_set, self.__get_character_position(character), ) if index > 0 \
                else (self.__get_character_position(character), )

        return pixel_set

    def __normalize_pixel_set(self, pixel_set):
        rows = [[] for _ in range(self.__dictionary.HEIGHT)]
        for character in pixel_set:
            for i in range(self.__dictionary.HEIGHT):
                rows[i] = rows[i] + character[i]

        return rows

    def __get_space_pixel_set(self):
        try:
            return getattr(self.__dictionary, 'space')
        except AttributeError:
            raise SystemExit('Space letter is not exists')

    def __get_character_position(self, character):

        try:
            return self.__dictionary.characters.get(character)
        except AttributeError:
            raise SystemExit('Dictionary characters\'re not exists')
