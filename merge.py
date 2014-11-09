#!/usr/bin/env python
import sys
rs = ''
for line in sys.stdin:
    line = line.strip()
    line = line.replace(";", '')
    items = line.split(',')
    if len(items) < 3:
        continue
    ret = float(items[2].replace('%', '')) 
    if  ret > 5 or ret < -5:
        continue
    rs += "%s,%s,%s;"%(items[0], items[1], items[2])
print "%s:%s"%('rmd', rs)

