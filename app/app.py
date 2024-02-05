import os
from bson.json_util import dumps
from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
application = Flask(__name__)
cache.init_app(application)

application.config["MONGO_URI"] = ('mongodb://' +
                                   os.environ['MONGO_INITDB_ROOT_USERNAME'] +
                                   ':' +
                                   os.environ['MONGO_INITDB_ROOT_PASSWORD'] +
                                   '@' +
                                   os.environ['MONGODB_HOSTNAME'] +
                                   ':27017/' +
                                   os.environ['MONGO_INITDB_DATABASE'] +
                                   "?authSource=admin")

mongo = PyMongo(application)
db = mongo.db


@application.route('/')
def index():
    return jsonify(
        status=True,
        message='Welcome to the Dockerized Flask MongoDB app!'
    )


@application.route('/predict', methods=['POST'])
@cache.cached(timeout=60)
def predict():
    data = request.get_json(force=True)
    list_of_ids = data["adIdList"]
    ctrs = db.estimated_ctr.find({"id": {"$in": list_of_ids}}, {'_id': False})
    return Response(
        dumps(list(ctrs)),
        mimetype='application/json'
    )


if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
