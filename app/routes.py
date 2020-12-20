from flask_restful import Resource
from . import api


class PostListApi(Resource):

    def get(self):
        return {"message": "Hello"}


api.add_resource(PostListApi, '/posts')
