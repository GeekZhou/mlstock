import memcache
import sys


for line in sys.stdin:
    rs = ''
    name = line.strip()
    f = open(name, 'r')
    name = name.split('.')[0].split('/')[1]
    i = 0
    rs = "%s,"%name
    records = f.readlines()
    if 90 > len(records):
        continue
    for j in range(1, 90):
        record = records[j]
        record = record.strip()
        record_list = record.split(',')
        for i in range(1, len(record_list)):
            rs += record_list[i] + ','
    print rs
    f.close()
