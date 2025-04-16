#!/usr/bin/env python2
import sys
import csv

def read_input(file):
    for line in file:
        yield list(csv.reader([line]))[0]

first_line = True
for columns in read_input(sys.stdin):
    if first_line:
        first_line = False  # skip header if needed
        continue
    try:
        gender = columns[4].strip().lower()
        age = columns[5].strip()
        if gender in ['male', 'female'] and age != '':
            print '%s\t%s' % (gender, age)
    except:
        continue

