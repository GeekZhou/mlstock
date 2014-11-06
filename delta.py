import sys
import os
import urllib2
cmd = "http://hq.sinajs.cn/list=sz%s"
name = sys.argv[1]
cmd = cmd%name
rs = urllib2.urlopen(cmd)
rs = rs.read()
items = rs.split(',')
now = float(items[3])
begin = float(items[1])
print (now - begin)/begin


