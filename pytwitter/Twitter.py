from pytwitter.User import User
from seleniumwrapper import WebDriver
import dataset


class Twitter(object):
    _base_url = "https://twitter.com/"

    driver = None
    database = None

    def __init__(self, database="sqlite:///twitter.db", driver=None):
        """
        initializes the twitter class
        if database is not None all users and tweet are getting cached in the database
        :param driver: selenium webdriver; default: None
        :param database: path to dataset database
        """
        if driver is not None:
            self.driver = driver
        else:
            self.driver = WebDriver.get_default()
        if database is not None:
            self.database = dataset.connect(database)

    def get_user(self, name):
        """
        fetches user object
        :param name: username
        :return: User object
        """
        user = User(self.driver, self._base_url, name)
        if self.database is not None:
            print(user.__dict__)
            # self.database["users"].insert(user.__dict__)
        return user

    def close(self):
        """
        closes the driver object
        :return: None
        """
        self.driver.close()
        self.driver.quit()
