#!/usr/bin/env python3
import datetime
import json
import distance
from parsec import *

def today():
    num = datetime.datetime.today().isoweekday()
    with open("recipes/{0}.json".format(num)) as file:
        return json.load(file)

def tommorrow():
    num = (datetime.datetime.today()+datetime.timedelta(days=1)).isoweekday()
    with open("recipes/{0}.json".format(num)) as file:
        return json.load(file)

def after_tommorrow():
    num = (datetime.datetime.today()+datetime.timedelta(days=2)).isoweekday()
    with open("recipes/{0}.json".format(num)) as file:
        return json.load(file)

def request(recipe, word):
    content = recipe["content"]
    return min(content, key=lambda item:distance.levenshtein(item[0], word)/float(len(item[0])))

def order(content):
    st = BasicState(content)
    recipe = choices(attempt(string("今天")).then(pack(("今天", today()))),
                    attempt(string("明天")).then(pack(("明天", tommorrow()))),
                    attempt(string("后天")).then(pack(("后天", after_tommorrow()))),
                    pack(("今天", today())))
    time = choices(attempt(string("早餐")), attempt(string("午餐")),
                    attempt(string("晚餐")), pack("午餐"))
    order_one = many(one).over(eof)
    @Parsec
    def helper(state):
        day, rcp = recipe(state)
        skip(space)(state)
        t = time(state)
        skip(space)(state)
        word = "".join(order_one(state)).rstrip()
        item = request(rcp, word)
        return day, t, item

    return helper(st)


if __name__ == '__main__':
    import pprint
    import sys
    pprint.pprint(order(" ".join(sys.argv[1:])))
