from unittest import TestCase

from source.bottle.BottleFactory import BottleFactory
from source.databaseManagers.BottleDatabaseManager import BottleDatabaseManager
from test.TestConstants import *
from test.databasesTools import clearAllDatabases


class BottleDatabasesTestCase(TestCase):

    def setUp(self):
        clearAllDatabases()

    def test_InsertOneBottleInEmptyBase(self):
        expectedBottle = BottleFactory().createBottle(dummy_name_1, dummy_vintage, dummy_type, dummy_price)

        BottleDatabaseManager.insertBottle(expectedBottle)

        bottleList = BottleDatabaseManager.listBottle()
        self.assertEqual(len(bottleList), 1)
        self.assertEqual(bottleList[0], expectedBottle)

    def test_InsertOneBottleInBaseContainingOneBottle(self):
        BottleDatabaseManager.insertBottle(
            BottleFactory.createBottle(dummy_name_1, dummy_vintage, dummy_type, dummy_price))

        expectedBottle = BottleFactory().createBottle(dummy_name_2, dummy_vintage, dummy_type, dummy_price)

        BottleDatabaseManager.insertBottle(expectedBottle)

        bottleList = BottleDatabaseManager.listBottle()
        self.assertEqual(len(bottleList), 2)
        self.assertEqual(bottleList[1], expectedBottle)

    def test_FirstBottleIdIs_1(self):
        self.assertEqual(BottleDatabaseManager.getCurrentIdBottle(), 1)

    def test_IncrementBottleIds(self):
        BottleDatabaseManager.incrementCurrentIdBottle()
        self.assertEqual(BottleDatabaseManager.getCurrentIdBottle(), 2)