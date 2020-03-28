from pytwitter.User import User
from seleniumwrapper import WebDriver
import dataset


class Twitter(object):
    _base_url = "https://twitter.com/"

    driver = None
    database = None

    def __init__(self, driver=None, database="sqlite:///twitter.db"):
        """
        initializes the twitter class
        if database is not None all users and tweet are getting cached in the database
        :param driver: selenium webdriver; default: None
        :param database: path to dataset database
        """
        self.driver = driver or WebDriver.get_default()
        if database is not None:
            self.database = dataset.connect(database)

    def get_user(self, name):
        """
        fetches user object
        :param name: username
        :return: User object
        """
        return User(self.driver, self._base_url, name)

    def close(self):
        """
        closes the driver object
        :return: None
        """
        self.driver.close()
