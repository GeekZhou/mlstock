#!/usr/bin/env python
import sys
import os
import urllib2
cmd = "http://hq.sinajs.cn/list=sz%s"
name = sys.argv[1]
if len(name) < 1:
    sys.exit(-1)
name = name.zfill(6)
cmd = cmd%name
rs = urllib2.urlopen(cmd)
rs = rs.read()
items = rs.split(',')
if len(items) < 3:
    sys.exit(-1)
now = float(items[3])
begin = float(items[1])
if begin < 0.1:
    sys.exit(-1)
print items[0].strip().split('"')[1].decode('gbk').encode('utf-8'),round((now - begin)/begin, 3)


