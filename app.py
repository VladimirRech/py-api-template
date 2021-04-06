from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)


# Classes
class Users(Resource):
    def get(self):
        data = pd.read_csv('./csv/users.csv')  # read the csv file
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code.

    def post(self):
        parser = reqparse.RequestParser()  # initialize

        parser.add_argument('userId', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('city', required=True)

        args = parser.parse_args()  # parse argumentos to dictionary

        # create new data frame containing new values
        new_data = pd.DataFrame({
            'userId': args['userId'],
            'name': args['name'],
            'city': args['city'],
            'locations': [[]]
        })

        # read our CSV
        data = pd.read_csv('./csv/users.csv')  # read the csv file
        # add the newly provided values
        data = data.append(new_data, ignore_index=True)
        # save back to CSV
        data.to_csv('./csv/users.csv', index=False)
        return {'data': data.to_dict()}, 200  # return data with 200 OK


class Locations(Resource):
    pass


# '/users' is our entry point for Users
api.add_resource(Users, '/users')
# '/locations' is our entry point for Locations
api.add_resource(Locations, '/locations')

# Control the app run and start
if __name__ == '__main__':
    app.run()  # run our Flask app
