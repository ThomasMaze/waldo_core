from source.bottle.Bottle import Bottle


def given_a_bottle(name, vintage, wineType, price):
    bottle = Bottle()
    bottle.name = name
    bottle.vintage = vintage
    bottle.type = wineType
    bottle.price = price
    return bottle
