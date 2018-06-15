import requests


class WSCall(object):

    @staticmethod
    def listBottle():
        return requests.get('http://localhost:5000/bottle/list')
