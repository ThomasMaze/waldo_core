#!/usr/bin/python
import sqlite3

print('Connecting to DB...')
connToBottleDB = sqlite3.connect('/Users/thomasmazaleyrat/PycharmProjects/waldo/waldo_core/databases_dumps/databases/BottleDatabase.db')

scriptFile = open('/Users/thomasmazaleyrat/PycharmProjects/waldo/waldo_core/databases_dumps/bottle_database_create.sql', 'r')
script = scriptFile.read()
scriptFile.close()

connToBottleDB.executescript(script)

connToBottleDB.commit()

connToBottleDB.close()
