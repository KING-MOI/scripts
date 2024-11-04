#!/usr/bin/env python3
import json, sys, collections
total = collections.Counter()
for line in open(sys.argv[1]):
    d = json.loads(line)
    total[d.get('model','?')] += d.get('usage',{}).get('total_tokens',0)
for k, v in total.items(): print(k, v)
