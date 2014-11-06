#!/usr/bin/env python
import sys
import os
import urllib2
def delta(name):
    cmd = "http://hq.sinajs.cn/list=sz%s"
    if len(name) < 1:
        return 0
    name = name.zfill(6)
    cmd = cmd%name
    rs = urllib2.urlopen(cmd)
    rs = rs.read()
    items = rs.split(',')
    if len(items) < 3:
        return 0
    name = items[0].strip().split('"')[1]
    now = float(items[3])
    begin = float(items[2])
    if begin < 0.1:
        return 0
    return name, "{:.2%}".format(round((now - begin)/begin, 4))

if __name__=='__main__':
    name = sys.argv[1]
    k, v = delta(name)
    print k.decode('gbk').encode('utf-8'), v
