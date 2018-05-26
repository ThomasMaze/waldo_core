import sqlite3

from source.bottle.BottleFactory import BottleFactory
from source.databaseManagers.DatabaseUtils import *


class DatabaseManager(object):

    @staticmethod
    def insertBottle(bottle,):
        conn = sqlite3.connect(databasesPath + 'BottleDatabase.db')

        query = "INSERT INTO bottle (id,name,vintage,type,price) " \
                "VALUES ({0},'{1}',{2},'{3}',{4});".format(1, bottle.name, bottle.vintage, bottle.type, bottle.price)
        conn.execute(query)
        conn.commit()
        conn.close()

    @staticmethod
    def listBottle():
        conn = sqlite3.connect(databasesPath + 'BottleDatabase.db')
        query = "SELECT * FROM bottle;"
        cursor = conn.execute(query)

        bottleList = []

        for row in cursor:
            bottleList.append(BottleFactory().createBottle(row[1], row[2], row[3], row[4]))

        conn.close()

        return bottleList
