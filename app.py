
from flask import Flask
from flask_restful import Api
# from flask_cors import CORS


"""
Local information storage
"""


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    # cors = CORS(app, resources={r"/*": {"origins": "*"}})

    app.config.from_object("config.Config")

    api = Api(app=app)

    from rewards.routes import routes

    routes(api=api)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
