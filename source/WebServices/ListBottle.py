from flask_restful import Resource

from Persistence.Persistence import Persistence


class List(Resource):

    @staticmethod
    def get():
        bottleList = Persistence.getBottleList()

        return {'status': 'success', 'data': bottleList}
