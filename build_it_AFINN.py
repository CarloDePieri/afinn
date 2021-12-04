#!/usr/bin/env python
import json
import requests

from os import remove


url = "https://raw.githubusercontent.com/marcellobarile/multilang-sentiment/develop/build/languages/AFINN-it.json"
json_file = "AFINN-it.json"
txt_file = "afinn/data/AFINN-it-165.txt"


r = requests.get(url, allow_redirects=True)
with open(json_file, "wb") as f:
    f.write(r.content)


data = {}
with open(json_file, "r") as f:
    data = json.load(f)

remove(json_file)

with open(txt_file, "a+") as f:
    for key in data.keys():
        f.write(f"{key}\t{data[key]}\n")


