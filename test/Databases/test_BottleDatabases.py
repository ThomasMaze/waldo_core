from unittest import TestCase

from source.bottle.BottleFactory import BottleFactory
from source.databaseManagers.DatabaseManager import DatabaseManager
from source.types.WineTypeEnum import WineTypeEnum
from test.TestConstants import *
from test.databasesTools import clearAllDatabases


class BottleDatabasesTestCase(TestCase):

    def setUp(self):
        clearAllDatabases()

    def test_InsertOneBottle(self):

        expectedBottle = BottleFactory().createBottle(dummy_name_1, dummy_vintage, WineTypeEnum.RED.value, dummy_price)

        DatabaseManager.insertBottle(expectedBottle)

        bottleList = DatabaseManager.listBottle()
        self.assertEqual(len(bottleList), 1)
        self.assertEqual(bottleList[0], expectedBottle)
