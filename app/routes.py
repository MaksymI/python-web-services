from flask_restful import Resource
from . import api
from . import models


class PostListApi(Resource):

    def get(self):
        return {"message": "Hello"}


api.add_resource(PostListApi, '/posts')
