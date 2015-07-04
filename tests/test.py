import sys, os
sys.path.insert(0, '..')
import unittest, tempfile, trendlinks, models

class TrendlinksTestCase(unittest.TestCase):

    def setUp(self):
        skip, db_location = tempfile.mkstemp()
        self.db = models.get_db(db_location)
        models.DATABASE = self.db
        self.app = trendlinks.app.test_client()
        models.initialize()

    def tearDown(self):
        self.db.close()

    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data

if __name__ == '__main__':
    unittest.main()
