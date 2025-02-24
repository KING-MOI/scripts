#!/usr/bin/env python3
import argparse, urllib.request, json, os, time
p = argparse.ArgumentParser()
p.add_argument('city', nargs='?', default='sf')
a = p.parse_args()
cache = os.path.expanduser('~/.cache/weather.json')
if os.path.exists(cache) and time.time() - os.path.getmtime(cache) < 1800:
    data = json.load(open(cache))
else:
    data = json.load(urllib.request.urlopen(f'https://wttr.in/{a.city}?format=j1'))
    json.dump(data, open(cache, 'w'))
c = data['current_condition'][0]
print(f"{c['temp_C']}C feels {c['FeelsLikeC']}C, {c['weatherDesc'][0]['value']}")
