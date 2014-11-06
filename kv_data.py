import memcache
import sys

s = memcache.Client(["218.244.128.35:11212"])
for line in sys.stdin:
    name = line.strip()
    print name
    f = open(name, 'r')
    name = name.split('.')[0].split('/')[1]
    for record in f.readlines():
        record = record.strip()
        records = record.split(',')
        date = records[0]
        print name+','+record
        key = "SZ_%s_%s"%(name, date)
        s.set(key, ','.join(records[1:]))
    f.close()
