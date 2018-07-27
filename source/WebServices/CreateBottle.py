from flask import request
from flask_restful import Resource

from Persistence.Persistence import Persistence


class Create(Resource):

    @staticmethod
    def get():
        if len(request.args['name']) > 20:
            return {'status': 'failure', 'message': " - invalid value for parameter 'name'"}

        Persistence.addBottle(request.args['name'])
        return {'status': 'success'}
