from flask_restful import Resource


class List(Resource):
    def get(self):
        return {'status': 'failure', 'data': []}




