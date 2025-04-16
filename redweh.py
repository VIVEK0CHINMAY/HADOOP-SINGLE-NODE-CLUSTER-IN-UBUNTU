#!/usr/bin/env python2
import sys

cold_days = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    key_value = line.split('\t', 1)
    if len(key_value) != 2:
        continue
    key, value = key_value
    try:
        temp = float(value)
        cold_days.append((key, temp))
    except:
        continue

# Sort by temperature (ascending)
cold_days.sort(key=lambda x: x[1])

# Print top 10 coldest days
for entry in cold_days[:10]:
    print "%s\t%.2f" % (entry[0], entry[1])
