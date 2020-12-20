from flask_restful import Resource
from flask import request
from marshmallow.exceptions import ValidationError
from . import api, db, schemas, models

post_schema = schemas.PostSchema()


class PostListApi(Resource):

    def post(self):
        try:
            post = post_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {"message": str(e)}, 400

        db.session.add(post)
        db.session.commit()
        return post_schema.dump(post), 201

    def get(self):
        posts = db.session.query(models.Post).all()
        return post_schema.dump(posts, many=True)


class PostApi(Resource):
    def get(self, uuid):
        post = db.session.query(models.Post).filter_by(uuid=uuid).first()
        if post is None:
            return "", 404
        return post_schema.dump(post), 200


api.add_resource(PostListApi, '/posts')
api.add_resource(PostApi, '/posts/<uuid>')
