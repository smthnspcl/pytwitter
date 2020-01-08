#!/usr/bin/python3
from os import pathsep
from sys import argv
import dataset
from seleniumwrapper.webdriver import WebDriver
from libs import User
from loguru import logger as log


class Configuration(object):
    users = []
    output = "out" + pathsep
    count = 1000

    @staticmethod
    def help():
        print("usage:")
        print("\tunix: ./twitter.py {arguments}")
        print("\twin:  .\\twitter.exe {arguments}")
        print("{arguments}\t\t\t{description}\t\t{default}")
        print("\t-u\t--username\tadd a username\t\tNone")
        print("\t-o\t--output\tset output dir\t\tout")
        print("\t-c\t--count\t\tcount of tweets\t\t1000")
        print("{example}")
        print(".\\twitter.exe -u s8n -u theydeadinside -o dankmemes")
        print("    \\-> executable|       \\-> 2nd username    \\-> output folder")
        print("                  \\-> 1st username")
        exit()

    @staticmethod
    def parse():
        c = Configuration()
        i = 0
        while i < len(argv):
            a = argv[i]
            if a in ["-u", "--username"]:
                c.users.append(argv[i + 1])
            elif a in ["-o", "--output"]:
                c.output = argv[i + 1]
            elif a in ["-c", "--count"]:
                c.count = int(argv[i + 1])
            elif a in ["-h", "--help"]:
                Configuration.help()
            i += 1
        if not c.output.endswith(pathsep):
            c.output += pathsep
        if len(c.users) == 0:
            Configuration.help()

        return c


if __name__ == '__main__':
    log.info("parsing arguments")
    args = Configuration.parse()
    log.info("opening database")
    db = dataset.connect("sqlite:///twitter.db")
    log.info("getting webdriver")
    d = WebDriver.get_default()
    for user in args.users:
        log.info("crea")
        u = User(d, user)
        u.get_steam_items(100)
    d.close()
