from flask import request
from werkzeug.security import check_password_hash
from . import app, db, models


@app.route('/login')
def login():
    auth = request.authorization
    if not auth:
        return "", 401, {"WWW-Authenticate": 'Basic realm="Authentication required"'}
    user = db.session.query(models.User).filter_by(login=auth.get("username", "")).first()
    if user is None or not check_password_hash(user.password, auth.get("password", "")):
        return "", 401, {"WWW-Authenticate": 'Basic realm="Authentication required"'}
    return ""  # потом сгенерируем JWT
