from pytwitter.User import User


class Twitter(object):
    _base_url = "https://twitter.com/"

    driver = None

    def __init__(self, driver, database="twitter.py"):
        self.driver = driver

    def get_user(self, name):
        return User(self.driver, self._base_url, name)
