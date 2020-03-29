from argparse import ArgumentParser
from pytwitter import Twitter


if __name__ == '__main__':
    ap = ArgumentParser()
    ap.add_argument("-u", "--username", "--usernames", action="append", nargs='+', required=True)
    ap.add_argument("-d", "--database", default="sqlite:///twitter.db", type=str)
    ap.add_argument("-c", "--count", default=100, type=int)
    a = ap.parse_args()
    twitter = Twitter(a.database)
    for user in a.username[0]:
        u = twitter.get_user(user)
        u.get_steam_items(a.count)
    twitter.close()
