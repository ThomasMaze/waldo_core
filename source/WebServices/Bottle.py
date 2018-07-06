from flask_restful import Resource


class List(Resource):

    @staticmethod
    def get():
        return {'status': 'success', 'data': []}
