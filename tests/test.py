import sys, os
sys.path.insert(0, '..')
import tempfile, trendlinks, models
from helpers import *

def setUp():
    app = trendlinks.app.test_client()

def tearDown():
    pass

def check_status_OK(url):
    """ Check that the URL returns a '200 OK' status """
    assert app.get(url).status_code == 200

def test_URLs_render():
    """ 
    Generate tests for a list of URLs.
    Pass if the URL does not return an error when sent a GET request.
    """
    URL_LIST = list_URLs()
    for url in URL_LIST:
        yield check_status_OK, url

if __name__ == '__main__':
    import nose
    nose.main()

