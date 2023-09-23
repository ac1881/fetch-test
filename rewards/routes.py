from flask_restful import Api
from rewards.views import ProcessApi, PointsApi


def routes(api: Api):

    api.add_resource(ProcessApi, "/receipts/process")
    api.add_resource(PointsApi, "/receipts/<id>/points")
