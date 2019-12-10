from selenium.webdriver import Firefox, FirefoxOptions
from user_agent import generate_navigator_js
from datetime import datetime
import dataset
from time import sleep

BASE_URL = "https://twitter.com/"


def scroll(driver, distance=50*1024):
    driver.execute_script("window.scrollTo(0, %i)" % distance)


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

    def __init__(self, driver, name):
        self.timestamp = datetime.now()
        self.name = name
        self.url = BASE_URL + name
        self._driver = driver

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

    def get_steam_items(self, c=1000):
        r = []

        for i in range(c):
            self._driver.execute_script("window.scrollTo(0, %i);" % (1024 * i))
            sleep(0.2)

        for item in self._driver.find_elements_by_class_name("tweet"):
            oc = item.find_element_by_class_name("content")
            item = {
                "timestamp": oc.find_element_by_class_name("stream-item-header").find_element_by_tag_name("small").text,
                "text": oc.find_element_by_class_name("js-tweet-text-container").text,
                "items": []
            }
            mcs = oc.find_elements_by_class_name("AdaptiveMediaOuterContainer")
            for mc in mcs:
                _item = {}
                if "is_video" in mc.find_element_by_class_name("AdaptiveMedia").get_attribute("class"):
                    _item["video"] = mc.find_element_by_tag_name("video").get_attribute("src")
                elif mc.find_elements_by_class_name("AdaptiveMedia-photoContainer"):
                    _item["image"] = mc.find_element_by_tag_name("img").get_attribute("src")
                item["items"].append(_item)
            r.append(item)
        return r


if __name__ == '__main__':

    db = dataset.connect("sqlite:///twitter.db")

    o = FirefoxOptions()
    o.add_argument("user-agent=%s" % generate_navigator_js(os=('mac', 'linux')))
    o.headless = True
    d = Firefox(executable_path="driver/geckodriver", firefox_options=o)

    for username in ["s8n"]:
        u = User(d, username)
        print(u.get_steam_items(1))
        # todo get until last known tweet
        # todo store in a well matchable scheme
        # username, uuid=src/txt+date, txt, src

    d.close()
