class Persistence(object):

    @staticmethod
    def getBottleList():
        file = open("/home/tmazaleyrat/PycharmProjects/waldo/waldo_core/persistency/bottle_persistency", "r")
        fileContent = file.read().splitlines()
        file.close()

        return fileContent

