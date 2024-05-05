#!/usr/bin/env python3
import urllib.request, json
d = json.load(urllib.request.urlopen('https://wttr.in/sf?format=j1'))['current_condition'][0]
print(f"{d['temp_C']}C feels {d['FeelsLikeC']}C, {d['weatherDesc'][0]['value']}")
