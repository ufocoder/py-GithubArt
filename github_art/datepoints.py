from datetime import datetime
from dateutil.relativedelta import relativedelta


class GithubDatePoints(object):
    MAX_HEIGHT = 7
    MAX_WIDTH = 51

    def __init__(self, pixel_set):
        self.__pixel_set = self.__normalize_pixel_set(pixel_set)
        self.__datetime_start_point = self.__get_datetime_start_point()

    def __normalize_pixel_set(self, pixel_set):
        size = min(len(pixel_set), self.MAX_HEIGHT)
        pixel_set = pixel_set[:size]
        for i in range(size):
            pixel_set[i] = pixel_set[i][:self.MAX_WIDTH]

        return pixel_set

    def __get_datetime_start_point(self):

        date_point = datetime.today()
        weekday = date_point.weekday()

        if weekday != 6:
            date_point = date_point - relativedelta(days=weekday, years=1)

        return date_point

    def get_date_points(self):

        dates = []
        for rows in range(len(self.__pixel_set)):
            for col in range(len(self.__pixel_set[rows])):
                if self.__pixel_set[rows][col] != 0:
                    dates.append(self.__datetime_start_point + relativedelta(weeks=col, days=rows))

        return dates
