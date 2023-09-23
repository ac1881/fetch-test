from flask import Response
from flask_restful import Resource
from flask import request, make_response
from rewards.services import calculate_rewards, id_generator, get_points

class ProcessApi(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for /receipts/process

        :return: JSON object
        """
        input_data = request.get_json()
        data = calculate_rewards(input_data)

        return make_response(data)

class PointsApi(Resource):
    @staticmethod
    def get(id) -> Response:
        """
        POST response method for /receipts/process

        :return: JSON object
        """
        points = get_points(id)

        data = {
            "points": points
        }

        return make_response(data)




