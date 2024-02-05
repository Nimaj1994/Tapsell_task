# Tapsell_task
requirements: this project needs docker as well as docker-compose and a stable internet connection

steps to run the project:
1. create a tapsell.env file from the template and add your preferred configurations
2. run the following command ` docker-compose up -d`
3. use `./import_csv.sh /your/csv/file/location` to import data to mongodb (you should follow the init.csv file format and use id and ctr as titles and ',' as delimiter)
4. now you cand send your requests to http://your_server_ip/
5. after about 15 minutes /stats/ endpoint will be ready to receive requests
6. (optional) you can use `./remove_all.sh` to delete all the changes on docker