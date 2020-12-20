import json
from unittest import mock

from app import app


def test_create_post():
    with mock.patch("app.db.session.add") as add, \
            mock.patch("app.db.session.commit") as commit:
        r = app.test_client().post('/posts', data=json.dumps(
            {
                "title": "Title1",
                "body": "body1",
                "date": "2010-04-01T00:00"
            }), content_type="application/json"
                                   )
        add.assert_called_once()
        commit.assert_called_once()
    assert r.status_code == 201
    assert r.json['title'] == "Title1"


def test_read_all_post():
    with mock.patch("app.db.session.query") as query:
        query.return_value.all.return_value = []
        r = app.test_client().get('/posts')
    assert r.status_code == 200
    assert len(r.json) == 0