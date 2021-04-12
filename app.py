from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)


# Classes
class Users(Resource):
    _usersFile = "./csv/users.csv"

    def get(self):
        data = pd.read_csv(self._usersFile)  # read the csv file
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code.

    def post(self):
        parser = reqparse.RequestParser()  # initialize

        parser.add_argument('userId', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('city', required=True)

        args = parser.parse_args()  # parse argumentos to dictionary

        # read our CSV
        data = pd.read_csv(self._usersFile)  # read the csv file

        if args['userId'] in list(data['userId']):
            return {
                'message': f"'{args['userId']}' already exists."
            }, 401
        else:
            # create new data frame containing new values
            new_data = pd.DataFrame({
                'userId': args['userId'],
                'name': args['name'],
                'city': args['city'],
                'locations': [[]]
            })

            # add the newly provided values
            data = data.append(new_data, ignore_index=True)
            # save back to CSV
            data.to_csv('./csv/users.csv', index=False)
            return {'data': data.to_dict()}, 200  # return data with 200 OK

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userId', required=True)
        parser.add_argument('location', required=True)
        args = parser.parse_args()

        data = pd.read_csv(self._usersFile)

        if args['userId'] in list(data['userId']):
            # evaluate string of lists to lists
            data['locations'] = data['locations'].apply(
                lambda x: ast.literal_eval(x)
            )

            data[data['userId'] == args['userId']].delete()

            # update users location
            user_data['locations'] = user_data['locations'].values[0].append(
                args['location'])

            # save back to CSV
            data.to_csv(self._usersFile, index=False)

            # return data and 200 OK
            return {'data': data.to_dict()}, 200

        else:
            # otherwise user does not exist
            return {
                'message': f"'{ args['userId'] }' user not found."
            }, 404

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userId', required=True)
        args = parser.parse_args()

        data = pd.read_csv(self._usersFile)

        if args['userId'] in list(data['userId']):
            # remove data entry matching given userId
            data = data[data['userId'] != args['userId']]

            # save back to CSV
            data.to_csv(self._usersFile, index=False)

            # return data and 200 OK
            return {'data': data.to_dict()}, 200

        else:
            return {
                'message': f"'{ args['userId'] }' user not found."
            }, 404


class Locations(Resource):
    pass


# '/users' is our entry point for Users
api.add_resource(Users, '/users')
# '/locations' is our entry point for Locations
api.add_resource(Locations, '/locations')

# Control the app run and start
if __name__ == '__main__':
    app.run()  # run our Flask app
