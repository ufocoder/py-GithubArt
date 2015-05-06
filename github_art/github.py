import subprocess
import os

from datepoints import GithubDatePoints
from pixelsets import LettersPixelSet


class Github(object):
    def __init__(self, string, cwd, dictionary):
        self.__string = string
        self.__dictionary = dictionary
        self.__cwd = os.path.abspath(cwd)
        self.commands = []

    def __git_init(self):
        self.commands.append(['git', 'init'])
        self.commands.append(['git', 'show-ref'])

    def __git_commit(self, datetime_point):
        # Date formats, URL: http://git-scm.com/docs/git-commit
        file = datetime_point.strftime("%Y-%m-%d_%H-%M-%S")
        date = datetime_point.strftime("%Y-%m-%d %H:%M:%S %z")

        self.commands.append(['touch', file])
        self.commands.append(['git', 'add', file])
        self.commands.append(['git', 'commit', '--message="' + file + '"', '--date="' + date + '"'])

    def initialite(self):

        pixel_set = LettersPixelSet(self.__string, self.__dictionary).get_pixel_set()
        date_points = GithubDatePoints(pixel_set).get_date_points()

        self.__git_init()

        for date_point in date_points:
            self.__git_commit(date_point)

    def set_account(self, username, proejct):
        github_url = 'https://' + username + '@github.com/' + username + '/' + proejct + '.git'
        self.commands.append(['git', 'remote', 'add', 'origin', github_url])
        self.commands.append(['git', 'push', '-u', 'origin', 'master'])

    def run(self):
        for command in self.commands:
            subprocess.call(command, cwd=self.__cwd)
