#!/usr/bin/env python
import sys
import os
import urllib2
def delta(id):
    cmd = "http://hq.sinajs.cn/list=sz%s"
    if len(id) < 1:
        return 
    id = id.zfill(6)
    cmd = cmd%id
    rs = urllib2.urlopen(cmd)
    rs = rs.read()
    items = rs.split(',')
    if len(items) < 3:
        return 
    name = items[0].strip().split('"')[1]
    now = float(items[3])
    begin = float(items[2])
    if begin < 0.1:
        return 
    rat = "{:.2%}".format(round((now - begin)/begin, 4))
    return id, name, rat 

if __name__=='__main__':
    id = sys.argv[1]
    a = delta(id)
    if not a:
        sys.exit(-1)
    q, k, v = a
    #print "%s,%s,%s;"%(q, k.decode('gbk').encode('utf-8'), v)
    sys.stdout.write("%s,%s,%s\n"%(q, k.decode('gbk').encode('utf-8'), v))
