from flask_restful import Resource
from flask import request
from . import api
from . import models


class PostListApi(Resource):

    def post(self):
        print(request.json)
        title = request.json['title']
        body = request.json['body']
        date = request.json['date']
        post = models.Post(title, body, date)
        db.sessions.add(post)
        db.sessions.commit()
        return {'title': title, 'body': body, 'date': date}, 201

    def get(self):
        return {"message": "Hello"}


api.add_resource(PostListApi, '/posts')
