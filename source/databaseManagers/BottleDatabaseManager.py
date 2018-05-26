import sqlite3

from source.bottle.BottleFactory import BottleFactory
from source.databaseManagers.DatabaseManager import DatabaseManager
from source.databaseManagers.DatabaseUtils import *


class BottleDatabaseManager(DatabaseManager):

    @staticmethod
    def insertBottle(bottle, ):
        conn = sqlite3.connect(databasesPath + 'BottleDatabase.db')

        currentId = BottleDatabaseManager.getCurrentIdBottle()
        BottleDatabaseManager.incrementCurrentIdBottle()
        query = "INSERT INTO bottle (id,name,vintage,type,price) " \
                "VALUES ({0},'{1}',{2},'{3}',{4});".format(currentId, bottle.name, bottle.vintage, bottle.type,
                                                           bottle.price)
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

    @staticmethod
    def getCurrentIdBottle():
        conn = sqlite3.connect(databasesPath + 'BottleDatabase.db')
        query = "SELECT cnt FROM currentId WHERE id=1;"
        cursor = conn.execute(query)
        currentId = cursor.fetchall()[0][0]

        conn.close()

        return currentId

    @staticmethod
    def incrementCurrentIdBottle():
        conn = sqlite3.connect(databasesPath + 'BottleDatabase.db')
        currentId = BottleDatabaseManager.getCurrentIdBottle()
        query = "UPDATE currentId SET cnt = {0} WHERE id=1;".format(currentId + 1)
        conn.execute(query)
        conn.commit()
        conn.close()
