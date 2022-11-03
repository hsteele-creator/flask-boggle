from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def test_display_board(self):
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data()
            self.assertEqual(res.status_code, 200)
        

