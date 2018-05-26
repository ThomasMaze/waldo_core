from source.bottle.Bottle import Bottle

class BottleFactory(object):

    @staticmethod
    def createBottle(name, vintage, wineType, price):
            bottle = Bottle()
            bottle.name = name
            bottle.vintage = vintage
            bottle.type = wineType
            bottle.price = price

            return bottle