from unittest import TestCase

from source.Persistence.Persistence import Persistence
from ..WSCall import WSCall


class ListBottleTestCase(TestCase):

    def setUp(self):
        file = open("/home/tmazaleyrat/PycharmProjects/waldo/waldo_core/persistency/bottle_persistency", "w")
        file.close()

    def test_Route(self):
        response = WSCall.listBottle()
        self.assertEqual(response.status_code, 200)

    def test_NoBottle(self):
        response = WSCall.listBottle()
        self.assertEqual('success', response.json()['status'])
        self.assertEqual(0, len(response.json()['data']))

    def test_OneBottle(self):

        Persistence.addBottle('bottle1')

        response = WSCall.listBottle()

        self.assertEqual('success', response.json()['status'])
        self.assertEqual('bottle1', response.json()['data'][0])

    def test_TwoBottles(self):

        Persistence.addBottle('bottle1')
        Persistence.addBottle('bottle2')

        response = WSCall.listBottle()

        self.assertEqual('success', response.json()['status'])
        self.assertEqual('bottle1', response.json()['data'][0])