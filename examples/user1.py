from pytwitter import Twitter

username = "s8n"
twitter = Twitter()  # initialize twitter object
user = twitter.get_user(username)  # get user via twitter object
print(user.__dict__)
twitter.close()  # close webdriver in twitter object
