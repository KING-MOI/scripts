#!/usr/bin/env python3
import urllib.request, json
print(json.load(urllib.request.urlopen('https://wttr.in/sf?format=j1'))['current_condition'][0]['temp_C'])
