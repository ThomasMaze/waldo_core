import requests


class WSCall(object):

    @staticmethod
    def listBottle():
        return requests.get('http://localhost:5000/bottle/list')

    @staticmethod
    def createBottle(name, vintage):
        return requests.get('http://localhost:5000/bottle/create?name=' + name + '&vintage=' + str(vintage))

    @staticmethod
    def emptyCreateBottle():
        return requests.get('http://localhost:5000/bottle/create')
