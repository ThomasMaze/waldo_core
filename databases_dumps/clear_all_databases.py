#!/usr/bin/python
import sqlite3

from source.databaseManagers.DatabaseUtils import databasesPath

print('Connecting to DB...')
connToBottleDB = sqlite3.connect(databasesPath + 'BottleDatabase.db')

scriptFile = open('~/PycharmProjects/waldo/waldo_core/databases_dumps/bottle_database_create.sql', 'r')
script = scriptFile.read()
scriptFile.close()

connToBottleDB.executescript(script)
connToBottleDB.commit()

connToBottleDB.close()
