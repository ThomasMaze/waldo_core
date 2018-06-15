from unittest import TestCase

from ..WSCall import WSCall


class ListBottleTestCase(TestCase):

    def test_Route(self):
        response = WSCall.listBottle()
        self.assertEqual(response.status_code, 200)

    def test_NoBottle(self):
        response = WSCall.listBottle()
        self.assertEqual('failure', response.json()['status'])
