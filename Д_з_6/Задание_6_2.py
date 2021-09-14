import sys

from routines import *


def correct_ranges(rb='', re=''):
    if rb.isdigit():
        rb = int(rb)
    else:
        rb = 0
    if re.isdigit():
        re = int(re)
    else:
        re = -1
    if rb - 1 <= 0:
        rb = 0
    else:
        rb = rb - 1
    if re != -1:
        re = rb + re
    return [rb, re]


if __name__ == "__main__":
    if len(sys.argv) > 2:
        offset_b = sys.argv[1]
        offset_e = sys.argv[2]
    elif len(sys.argv) > 1:
        offset_b = sys.argv[1]
        offset_e = '#'
    else:
        offset_b = '#'
        offset_e = '#'
else:
    offset_b = '#'
    offset_e = '#'

ranges = correct_ranges(offset_b, offset_e)

with open(get_database_file(), mode='r', encoding='UTF8') as f:
    records = ((r.lstrip().rstrip().replace(chr(0), '')) for r in f.readlines())
    result_set = list(records)
    if ranges[1] == -1:
        print('\n'.join(result_set[ranges[0]::]))
    else:
        print('\n'.join(result_set[ranges[0]:ranges[1]:]))