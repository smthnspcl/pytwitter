from datetime import datetime
from time import sleep
from progressbar import ProgressBar
from .Tweet import Tweet


class RetardedUserError(Exception):
    @staticmethod
    def throw(msg):
        raise RetardedUserError(msg)


class User(object):
    _driver = None

    timestamp = None
    url = None
    name = None
    full_name = None
    description = None
    location = None
    website = None
    joined = None
    media = None
    picture = None
    banner = None
    tweets = []

    def __init__(self, driver, name, base_url="https://twitter.com/"):
        """
        initializes the user object
        :param driver: selenium webdriver
        :param name: twitter username
        :param base_url: _base_url in Twitter object
        """
        self.timestamp = datetime.now()
        self.name = name
        self.url = base_url + name
        self._driver = driver
        print(self.url)

        self._driver.get(self.url)

        self.full_name = self._driver.find_element_by_class_name("ProfileHeaderCard-nameLink").text
        self.banner = self._driver.find_element_by_class_name("ProfileCanopy-headerBg") \
            .find_element_by_tag_name("img").get_attribute("src")
        self.picture = self._driver.find_element_by_class_name("ProfileAvatar-container") \
            .find_element_by_tag_name("img").get_attribute("src")
        self.description = self._driver.find_element_by_class_name("ProfileHeaderCard-bio").text
        self.location = self._driver.find_element_by_class_name("ProfileHeaderCard-locationText").text
        self.website = self._driver.find_element_by_class_name("ProfileHeaderCard-urlText").text
        self.joined = self._driver.find_element_by_class_name("ProfileHeaderCard-joinDateText").text

    def get_stream_items(self, c=1000, download_path=None):
        """
        fetches all items of a users stream
        :param c: count of times the webdriver should scroll down
        :param download_path: if specified all media gets downloaded
        :return: list of Tweet
        """
        download_media = download_path is not None
        r = []
        with ProgressBar(max_value=c) as pb:
            for i in range(c):
                self._driver.execute_script("window.scrollTo(0, %i);" % (1024 * i))
                pb.update(i)
                sleep(0.2)

        for item in self._driver.find_elements_by_class_name("tweet"):
            oc = item.find_element_by_class_name("content")
            t = Tweet()
            t.set_timestamp(oc.find_element_by_class_name("stream-item-header").find_element_by_tag_name("small").text)
            t.text = oc.find_element_by_class_name("js-tweet-text-container").text
            if download_media:
                mcs = oc.find_elements_by_class_name("AdaptiveMediaOuterContainer")
                for mc in mcs:
                    _item = {}
                    if "is_video" in mc.find_element_by_class_name("AdaptiveMedia").get_attribute("class"):
                        _item["video"] = mc.find_element_by_tag_name("video").get_attribute("src")
                        print(_item["video"])
                    elif mc.find_elements_by_class_name("AdaptiveMedia-photoContainer"):
                        _item["image"] = mc.find_element_by_tag_name("img").get_attribute("src")
                        print(_item["image"])
                    t.items.append(_item)
            r.append(t)
        self.tweets = r
        return r
