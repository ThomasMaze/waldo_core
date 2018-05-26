from unittest import TestCase

from source.bottle.BottleFactory import BottleFactory
from test.TestConstants import *
from test.bottleTools import given_a_bottle


class BottleFactoryTestCase(TestCase):

    def test_Nominal(self):

        expectedBottle = given_a_bottle(dummy_name_1, dummy_vintage, dummy_type, dummy_price)

        effectiveBottle = BottleFactory().createBottle(dummy_name_1, dummy_vintage, dummy_type, dummy_price)

        self.assertEqual(expectedBottle, effectiveBottle)
