# Getting Started
To Run Graylog separatly we need to run elasticsearch and mongodb separatly and then configure es and mongodb details in 
docker-compose.yml. If elasticsearch and mongodb is running somewhere you can configure both details with glraylog else there we will run elasticsearch and mongodb with docker separatly and configure with glraylog.

In the graylog_separate_image project directory, follow the given steps to run GrayLog service separatly:

   1. Rename sample.env to .env and Configure .evn file
   2. Containerize the App with Docker
   3. Runs the elastic-search app in the development mode > sudo docker-compose -f elastic-search.yml up
   4. Runs the mongodb app in the development mode > sudo docker-compose -f mongodb.yml up

   5. Once the both elastic-search and mongodb run update .env file with mongodb and es details
   6. Runs the graylob app in the development mode > sudo docker-compose up
   7. Open [http://localhost:9000/] to Test GrayLog it in your browser.



