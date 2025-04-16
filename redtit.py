#!/usr/bin/env python2
import sys

current_gender = None
total_age = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()
    gender, age = line.split('\t', 1)
    try:
        age = float(age)
    except ValueError:
        continue

    if current_gender == gender:
        total_age += age
        count += 1
    else:
        if current_gender:
            avg = total_age / count if count > 0 else 0
            print '%s\t%.2f' % (current_gender, avg)
        current_gender = gender
        total_age = age
        count = 1

# Don't forget the last key
if current_gender:
    avg = total_age / count if count > 0 else 0
    print '%s\t%.2f' % (current_gender, avg)

