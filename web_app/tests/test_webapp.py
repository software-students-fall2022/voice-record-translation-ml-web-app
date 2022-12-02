import unittest
from flask import current_app
from controller import app,get_db


class Test_Web_App(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.appctx = self.app.app_context()
        self.appctx.push()

    def tearDown(self):
        self.appctx.pop()
        self.app = None
        self.appctx = None

    def test_app(self):
        assert self.app is not None
        assert current_app == self.app

    def test_db(self):
        db=get_db()
        print(db.list_collection_names)
        s=db.list_collection_names
        assert db.list_collection_names==s
