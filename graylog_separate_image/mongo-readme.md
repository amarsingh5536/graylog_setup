# Login mongo via root passowrd 
mongosh -u root -p rootpassword --authenticationDatabase admin

# create db graylog
use graylog

#  Create user for deployment and grant readWrite permission to user of database graylog
db.createUser(
  {
    user: "dev",
    pwd:  "dev123",
    roles: [ { role: "readWrite", db: "graylog" },
             { role: "read", db: "test" } ]
  }
)

# Mongodb URI for graylog:
MONGODB_URI=mongodb://dev:dev123@192.168.253.18:27018/graylog