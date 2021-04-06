from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)


# Classes
class Users(Resource):
    pass


class Locations(Resource):
    pass


# '/users' is our entry point for Users
api.add_resource(Users, '/users')
# '/locations' is our entry point for Locations
api.add_resource(Locations, '/locations')

# Control the app run and start
if __name__ == '__main__':
    app.run()  # run our Flask app