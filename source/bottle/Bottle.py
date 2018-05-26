class Bottle(object):
    name = None
    vintage = None
    type = None
    price = None

    def __eq__(self, other):
        self.name = other.name
        self.vintage = other.vintage
        self.type = other.type
        self.price = other.price
