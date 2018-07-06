from unittest import TestCase

from source.Persistence import Persistence
from ..WSCall import WSCall


class ListBottleTestCase(TestCase):

    def test_Route(self):
        response = WSCall.listBottle()
        self.assertEqual(response.status_code, 200)

    def test_NoBottle(self):
        response = WSCall.listBottle()
        self.assertEqual('success', response.json()['status'])
        self.assertEqual(0, len(response.json()['data']))

    def test_OneBottle(self):

        response = WSCall.listBottle()

        self.assertEqual('success', response.json()['status'])
        self.assertEqual('bottle1', response.json()['data'][0])