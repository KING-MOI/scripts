#!/usr/bin/env python3
# grew into tokentally
import json, sys, collections
by_day = collections.defaultdict(collections.Counter)
for line in open(sys.argv[1]):
    try:
        d = json.loads(line)
    except json.JSONDecodeError:
        continue
    day = d.get('timestamp','')[:10]
    by_day[day][d.get('model','?')] += d.get('usage',{}).get('total_tokens',0)
for day in sorted(by_day):
    print(day, sum(by_day[day].values()))
