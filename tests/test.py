import sys
sys.path.insert(0, '..')
import tempfile, models, html, os, unittest
import thing as trendlinks
import logging as log
from flask.ext.login import current_user
from helpers import *
from peewee import SqliteDatabase
from nose import *
from nose.tools import nottest


class TestTrendlinks(object):

    @classmethod
    def setUpClass(self):
        self.db, self.db_name = tempfile.mkstemp()
        trendlinks.app.config['TESTING'] = True
        trendlinks.app.config['WTF_CSRF_ENABLED'] = False
        self.app = trendlinks.app.test_client()
        with trendlinks.app.app_context():
            models.initialize(self.db_name)

    @classmethod
    def tearDownClass(self):
        os.close(self.db)
        os.unlink(self.db_name)

    def check_status_OK(self, url):
        """ Check that the URL returns a '200 OK' status """
        redirected_status_code = (
            self.app
            .get(url, follow_redirects=True)
            .status_code
        )
        assert redirected_status_code == 200

    def test_URLs_render(self):
        """
        Generate tests for a list of URLs.
        Pass if the URL does not return an error when sent a GET request.
        """
        URL_LIST = list_URLs(self.app)
        for url in URL_LIST:
            log.debug('Rendering {}'.format(url))
            yield self.check_status_OK, url

    def test_bad_login(self):
        """
        Test that a User receives a fail message with bad password.
        """
        fail_message = "Your email or password doesn't match."
        r = self.login('user@cool.io', 'wrongpass')
        response_string = html.unescape(r.get_data().decode('utf8'))
        assert fail_message in response_string

    def test_good_register(self):
        """
        Test that you can register to the site.
        Pass if the new user exists.
        """
        test_email = 'user@cool.io'
        self.register(test_email, 'securepass')
        self.login(test_email, 'securepass')
        assert True

    def test_good_login(self):
        """
        Test that a registered User can log in to the site.
        Passes if the User is redirected to the members page.
        """
        test_email = 'jake@cool.io'
        self.register(test_email, 'securepass')
        response = self.login(test_email, 'securepass')
        redirect_url = get_url_for('members')
        assert response.headers.get('location') == redirect_url


    def test_good_logout(self):
        """
        Test that a logged-in user can log out of the site.
        """
        self.app.get('/logout')
        pass

    def test_duplicate_register(self):
        """
        Tests that you can't register with the same email twice.
        """
        dupe_message = 'User with that email already exists.'
        self.register('popular@gmail.com', 'mypass')
        response = self.register('popular@gmail.com', 'someotherpass')
        response_string = html.unescape(response.get_data().decode('utf8'))
        assert dupe_message in response_string

    def test_stay_logged_in(self):
        """
        Can we log in, and stay logged in after the redirect?
        """
        with self.app:
            email = 'jake@cool.io'
            self.login(email, 'securepass')
            assert current_user.email == email

    def login(self, email, password):
        """
        Do a login.
        """
        return self.app.post('/', data=dict(
            email=email,
            password=password
        ), follow_redirects=False)

    def register(self, email, password):
        """
        Do a registration.
        """
        return self.app.post('/register', data=dict(
            email=email,
            password=password,
            password2=password
        ), follow_redirects=False)

if __name__ == '__main__':
    import nose
    nose.main()

