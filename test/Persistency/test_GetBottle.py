from unittest import TestCase

import os

from source.Persistence.Persistence import Persistence


class GetBottleTestCase(TestCase):

    def setUp(self):
        file = open("/home/tmazaleyrat/PycharmProjects/waldo/waldo_core/persistency/bottle_persistency", "w")
        file.close()

    def test_FileExistance(self):
        self.assertTrue(os.path.exists("/home/tmazaleyrat/PycharmProjects/waldo/waldo_core/persistency/bottle_persistency"))

    def test_FileShouldBeEmptyIfNoBottle(self):
        self.assertEqual([], Persistence.getBottleList())

    def test_FileContainsOneLineShouldReturnBottleName(self):
        self.givenABottle('bottle')

        self.assertEqual(['bottle'], Persistence.getBottleList())

    def test_FileContainsOneLineShouldReturnBottleName_OtherCase(self):
        self.givenABottle('bottle1')

        self.assertEqual(['bottle1'], Persistence.getBottleList())


    def test_FileContainsTwoLinesShouldReturnBottlesName(self):
        self.givenABottle('bottle1')
        self.givenABottle('bottle2')

        self.assertEqual(['bottle1', 'bottle2'], Persistence.getBottleList())


    #########
    # Given #
    #########

    def givenABottle(self, bottleName):
        file = open("/home/tmazaleyrat/PycharmProjects/waldo/waldo_core/persistency/bottle_persistency", "a")
        file.write(bottleName + '\n')
        file.close()
