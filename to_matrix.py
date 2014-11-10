#!/usr/bin/env python
import memcache
import sys

'''
    input/000001.csv... -> matrix.csv
'''

for line in sys.stdin:
    rs = ''
    name = line.strip()
    f = open(name, 'r')
    name = name.split('.')[0].split('/')[1]
    i = 0
    rs = "%s,"%name
    records = f.readlines()
    '''
        the days of record must above 90, else it is too sparse
    '''
    if 90 > len(records):
        continue
    for j in range(1, 90):
        record = records[j]
        record = record.strip()
        record_list = record.split(',')
        '''
            Date,Open,High,Low,Close,Volume,Adj Close
        '''
       # for i in range(1, len(record_list)):
       #     rs += record_list[i] + ','
        Open = float(record_list[1])
        Close = float(record_list[6])
        rs += str(round((Open - Close)/Close, 6)) + ','
    print rs
    f.close()
