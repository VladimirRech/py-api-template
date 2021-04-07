# get users
curl http://127.0.0.1:5000/users

# post new user

# JSON
curl -d '{ "userId": "322", "name": "Wayne", "city": "Gothan" }' -H 'Content-Type: application/json' -X POST http://127.0.0.1:5000/users
# WITH PARAMETERS
curl -d "userId=321&name=Vlad&city=Transilvania" -X POST http://localhost:5000/users
