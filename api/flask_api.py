from flask import Flask
from flask_restful import Api
from views import ClassPlanner

app = Flask(__name__)
api = Api(app)

# add API endpoints
api.add_resource(ClassPlanner, '/', '/schedule')
