from unittest import TestCase

from source.Persistence.Persistence import Persistence


class AddBottleTestCase(TestCase):

    def setUp(self):
        file = open("/home/tmazaleyrat/PycharmProjects/waldo/waldo_core/persistency/bottle_persistency", "w")
        file.close()

    def test_addingOneBottleFromEmptyFile(self):

        Persistence.addBottle('bottle1')

        self.assertEqual(['bottle1'], Persistence.getBottleList())

    def test_addingOneBottleFromNotEmptyFile(self):

        Persistence.addBottle('bottle1')
        Persistence.addBottle('bottle2')

        self.assertEqual(['bottle1', 'bottle2'], Persistence.getBottleList())