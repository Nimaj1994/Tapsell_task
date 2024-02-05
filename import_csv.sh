docker cp "$1" mongodb:./data.csv
docker exec mongodb /bin/sh -c 'mongoimport --db ctr_db --collection estimated_ctr --type csv --headerline --authenticationDatabase admin --username "$MONGO_INITDB_ROOT_USERNAME" --password "$MONGO_INITDB_ROOT_PASSWORD" --drop --file ./data.csv'
