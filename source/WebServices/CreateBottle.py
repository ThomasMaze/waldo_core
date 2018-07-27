from flask import request
from flask_restful import Resource


class Create(Resource):

    @staticmethod
    def get():
        if len(request.args['name']) > 20:
            return {'status': 'failure', 'message': " - invalid value for parameter 'name'"}

        return {'status': 'success'}
