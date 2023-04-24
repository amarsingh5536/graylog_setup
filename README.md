# GRAYLOG.
Graylog is Open source log management system helps to you collect and indexing, and analyzing logs data.
Refrence: https://go2docs.graylog.org/

# ElasticSearch.
Graylog uses the ElasticSearch to storing logs and searching text. All the logs data store in elasticsearch.
Loss of the elasticsearch we loss the logs data.

# MongoDb.
Graylog uses the mongodb only storing meta information such as user information and stream configurations etc.

# Graypy:
Graypy is python library to help you send log messages in graylog.
Refrence: https://pypi.org/project/graypy/

# Graylog2:
Graylog2 is node.js package to help you send log messages in graylog.
Refrence: https://www.npmjs.com/package/graylog2


# Getting Started
In the project directory, follow the given steps to run GrayLog service:

   1. Rename sample.env to .env and Configure .evn file
   2. Containerize the App with Docker
   3. Runs the app in the development mode > sudo docker-compose up
   4. Open [http://localhost:9000/] to Test GrayLog it in your browser.
   5. Login web ui with user:admin password:Dev@123

# Create GRAYLOG_ROOT_PASSWORD_SHA2 passowrd
   You can create GRAYLOG_ROOT_PASSWORD_SHA2 encrypted passowrd using this command:
   echo -n 'Dev@143' | sha256sum

   Now you can login web ui with user:admin password:Dev@143


# How to check GELF UDP LOGS
   1. Open [http://localhost:9000/] to Test GrayLog it in your browser.
   2. Go to system and inputs and select option input.
   3. Launch new input with GELF UDP.
   4. Create logs via logger.
   5. Open Show received messages of new launched input.
