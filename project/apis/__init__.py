from flask_restx import Api

from project.apis.alive import alive_namespace


api = Api(version="1.0", title="Project Name", doc="/docs")

api.add_namespace(alive_namespace, path="/alive")
