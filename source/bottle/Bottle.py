class Bottle(object):
    name = None
    vintage = None
    type = None
    price = None

    def __eq__(self, other):
        return self.name == other.name and \
               self.vintage == other.vintage and \
               self.type == other.type and \
               self.price == other.price
