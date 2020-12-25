import datetime
from flask import request, jsonify
from werkzeug.security import check_password_hash
import jwt
from . import app, db, models

SECRET_KEY = app.config['SECRET_KEY']
AUTH_REQUIRED = "", 401, {"WWW-Authenticate": 'Basic realm="Authentication required"'}

@app.route('/login')
def login():
    auth = request.authorization
    if not auth:
        return AUTH_REQUIRED
    user = db.session.query(models.User).filter_by(login=auth.get("username", "")).first()
    if user is None or not check_password_hash(user.password, auth.get("password", "")):
        return AUTH_REQUIRED
    token = jwt.encode({
        "user_id": user.uuid,
        "exp": datetime.datetime.now() + datetime.timedelta(hours=1)
    }, SECRET_KEY)
    return jsonify({"token": token.decode('utf-8')})


def token_required(f):
    def wrapper(self, *args, **kwargs):
        token = request.headers.get("X-Api-Key", "")
        if not token:
            return AUTH_REQUIRED
        try:
            uuid = jwt.decode(token, SECRET_KEY)['user_id']
        except (KeyError, jwt.ExpiredSignatureError):
            return AUTH_REQUIRED
        user = db.session.query(models.User).filter_by(uuid=uuid).first()
        if not user:
            return AUTH_REQUIRED
        return f(self, user, *args, **kwargs)
    return wrapper

