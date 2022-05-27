#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL= "http://127.0.0.1:2224/"

resp= requests.get(URL)

# pretty-print the response back from our POST request
hero = resp.json()

print("The Hero name is: {0}".format( hero[0]["name"]))
print("Real name is: {0}".format( hero[0]["realName"]))
print("Started since:  {0}".format( hero[0]["since"]))
print("The Hero Powers are : ")
for power in hero[0]["powers"]:
    print("==> {0}".format( power))

