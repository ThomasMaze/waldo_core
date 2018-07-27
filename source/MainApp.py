from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from WebServices.ListBottle import List
from WebServices.CreateBottle import Create

waldo = Flask(__name__)
CORS(waldo)
waldoApi = Api(waldo)

waldoApi.add_resource(List, '/bottle/list')

waldoApi.add_resource(Create, '/bottle/create')

if __name__ == '__main__':
    waldo.run(port=5000, debug=True)
