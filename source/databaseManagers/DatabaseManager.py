import sqlite3

from source.databaseManagers.DatabaseUtils import *


class DatabaseManager(object):

    @staticmethod
    def connectToBottleDatabase():
        conn = sqlite3.connect(databasesPath + 'BottleDatabase.db')
        return conn
