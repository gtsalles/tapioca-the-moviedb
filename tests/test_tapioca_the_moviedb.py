# coding: utf-8

import unittest

from tapioca_the_moviedb import TheMovieDB


class TestTapiocaTheMoviedb(unittest.TestCase):

    def setUp(self):
        self.wrapper = TheMovieDB()


if __name__ == '__main__':
    unittest.main()
