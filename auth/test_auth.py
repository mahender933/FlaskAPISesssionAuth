import json
import sys
import unittest

sys.path.append("..")

from manage import app, db


class SignupTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = app.test_client()
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_signup_endpoint(self):
        payload = json.dumps({
            "username": "tester",
            "email": "tester@test.com",
            "password": "test1#"
        })
        response = self.client.post('/sign-up', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(201, response.status_code)
        # Sign Up Validation Test Cases
        # New sign up with same payload i.e same username
        response = self.client.post('/sign-up', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(409, response.status_code)  # User already exists with same username
        # Bad email
        response = self.client.post('/sign-up', headers={"Content-Type": "application/json"}, data=json.dumps({
            "username": "tester1",
            "email": "tester1",
            "password": "test1#"
        }))
        self.assertEqual(422, response.status_code)
        # Digit required in password
        response = self.client.post('/sign-up', headers={"Content-Type": "application/json"}, data=json.dumps({
            "username": "tester1",
            "email": "tester1",
            "password": "test"
        }))
        self.assertEqual(422, response.status_code)
        # Special character required in password
        response = self.client.post('/sign-up', headers={"Content-Type": "application/json"}, data=json.dumps({
            "username": "tester1",
            "email": "tester1",
            "password": "test1"
        }))
        self.assertEqual(422, response.status_code)

    def tearDown(self):
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()
