import sys, os
sys.path.insert(0, '..')
import tempfile, trendlinks, models

def setUp():
    skip, db_location = tempfile.mkstemp()
    db = models.get_db(db_location)
    models.DATABASE = db
    app = trendlinks.app.test_client()
    models.initialize()

def tearDown():
    db.close()

def check_status_OK(self, url):
    app.get(url)

