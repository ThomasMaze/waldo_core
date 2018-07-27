from unittest import TestCase

from source.Persistence.Persistence import Persistence
from ..WSCall import WSCall


class CreateBottleTestCase(TestCase):

    def setUp(self):
        file = open("/home/tmazaleyrat/PycharmProjects/waldo/waldo_core/persistency/bottle_persistency", "w")
        file.close()

    def test_Route(self):
        response = WSCall.createBottle("", -1)
        self.assertEqual(200, response.status_code)

    def test_ValidParameters(self):
        response = WSCall.createBottle("persevero", 2017)

        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(['persevero'], Persistence.getBottleList())

    def test_TooLongName(self):
        tooLongBottleName = "IamATooLongBottleName------------------------"

        response = WSCall.createBottle(tooLongBottleName, 2017)
        self.assertEqual(response.json()['status'], 'failure')
        self.assertEqual(response.json()['message'], " - invalid value for parameter 'name'")

