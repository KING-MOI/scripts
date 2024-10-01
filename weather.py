#!/usr/bin/env python3
import argparse, urllib.request, json
p = argparse.ArgumentParser()
p.add_argument('city', nargs='?', default='sf')
a = p.parse_args()
d = json.load(urllib.request.urlopen(f'https://wttr.in/{a.city}?format=j1'))['current_condition'][0]
print(f"{d['temp_C']}C feels {d['FeelsLikeC']}C, {d['weatherDesc'][0]['value']}")
