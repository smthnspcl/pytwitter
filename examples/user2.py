from pytwitter import User
from seleniumwrapper import WebDriver

username = "s8n"
d = WebDriver.get_default()
user = User(d, username)
print(user.__dict__)
d.close()
