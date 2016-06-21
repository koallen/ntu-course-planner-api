from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from course_planner.planner import Planner

class PlannerApi(Resource):
    def get(self):
        # parse query parameters
        parser = RequestParser()
        parser.add_argument('course', type=str, required=True, help='List of course codes', action='append')
        args = parser.parse_args()

        planner = Planner()
        result = planner.plan(args['course'])
        return result
