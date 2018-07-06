from flask import Flask
from flask_restful import Api

from WebServices.Bottle import List

waldo = Flask(__name__)
waldoApi = Api(waldo)

waldoApi.add_resource(List, '/bottle/list')

if __name__ == '__main__':
    waldo.run(port=5000, debug=True)
