import sys, os
sys.path.insert(0, '..')
import tempfile, trendlinks, models
from helpers import *
from nose import *

class TestTrendlinks(object):

    @classmethod
    def setUpClass(self):
        self.app = trendlinks.app.test_client()

    @classmethod
    def tearDownClass(self):
        pass

    def check_status_OK(self, url):
        """ Check that the URL returns a '200 OK' status """
        assert self.app.get(url).status_code == 200

    def test_URLs_render(self):
        """ 
        Generate tests for a list of URLs.
        Pass if the URL does not return an error when sent a GET request.
        """
        URL_LIST = list_URLs(self.app)
        for url in URL_LIST:
            yield check_status_OK, url

if __name__ == '__main__':
    import nose
    nose.main()

