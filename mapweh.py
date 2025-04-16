#!/usr/bin/env python2
import sys

for line in sys.stdin:
    if not line.strip():
        continue

    try:
        date = line[6:14]
        temp_min = float(line[47:53].strip())

        if temp_min < 15.0:
            # Format date to yyyy/mm/dd
            formatted_date = "%s/%s/%s" % (date[:4], date[4:6], date[6:])
            print "The Day is Cold Day :%s\t%.2f" % (formatted_date, temp_min)

    except:
        continue
