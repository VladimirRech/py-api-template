# get users
curl http://127.0.0.1:5000/users

# post new user
curl -d '{ "userId": "321", "name": "Vlad", "city": "Transilvania" }' http://127.0.0.1:5000/users