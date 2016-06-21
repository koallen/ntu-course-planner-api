from flask import Flask
from flask_restful import Api
from views import PlannerApi

app = Flask(__name__)
api = Api(app)

# add API endpoints
api.add_resource(PlannerApi, '/schedule')
