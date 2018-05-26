from source.bottle.Bottle import Bottle


class BottleFactory(object):

    @staticmethod
    def createBottle(name, vintage, type, price):
        bottle = Bottle()
        bottle.name = name
        bottle.vintage = vintage
        bottle.type = type
        bottle.price = price

        return bottle

