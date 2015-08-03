from models import *
from nose.tools import raises
import datetime, os, tempfile, trendlinks, unittest

class TestDatabase(object):

    @classmethod
    def setUpClass(self):
        """Create and init a fake database for testing."""
        self.db, self.db_name = tempfile.mkstemp()
        trendlinks.app.config['TESTING'] = True
        self.app = trendlinks.app.test_client()
        with trendlinks.app.app_context():
            trendlinks.initialize_database(self.db_name)

    @classmethod
    def tearDownClass(self):
        """Close the db file, and remove the db from the filesystem."""
        os.close(self.db)
        os.unlink(self.db_name)

    def test_create_user_success(self):
        """Can we successfully create a User directly from the model?"""
        User.create_user(
            email='tim@gmail.com',
            password='sosecure2',
            admin=False
        )

    @raises(ValueError)
    def test_create_user_already_exists(self):
        """Does creating a duplicate User actually raise an error?"""
        User.create_user(
            email='jim@gmail.com',
            password='sosecure1',
        )

        User.create_user(
            email='jim@gmail.com',
            password='somethingelse',
        )

    def test_create_user_profile_success(self):
        """Can we create a UserProfile directly from the model?"""
        birthdate = datetime.date(1908, 11, 2)
        email = 'travis@trendlinks.com'

        User.create_user(
            email=email,
            password='iusethispasswordeverywhere',
        )

        user = User.get(User.email == email)

        UserProfile.create_user_profile(
            user=user,
        )

        # if everything passed, pass the test
        assert True

    def test_retrieve_user(self):
        """Can we retrieve a created User?"""
        email = 'a@b.cd'
        User.create_user(
            email=email,
            password='efg',
        )

        the_user = User.get(User.email == email)
        assert type(the_user) == User

    @unittest.skip('Have to finish this')
    def test_retrieve_user_profile(self):
        """Can we retrive a created UserProfile?"""
        UserProfile.create_user_profile(
        )
