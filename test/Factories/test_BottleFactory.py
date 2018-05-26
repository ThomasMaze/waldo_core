from unittest import TestCase

from source.bottle.Bottle import Bottle
from source.bottle.BottleFactory import BottleFactory
from source.types.WineTypeEnum import WineTypeEnum


class BottleFactoryTestCase(TestCase):

    def test_Nominal(self):

        expectedBottle = Bottle()
        expectedBottle.name = "dummy_name"
        expectedBottle.vintage = 2014
        expectedBottle.type = WineTypeEnum.RED
        expectedBottle.price = 35

        effectiveBottle = BottleFactory().createBottle("dummy_name", 2014, WineTypeEnum.RED, 35)

        self.assertEqual(expectedBottle, effectiveBottle)
