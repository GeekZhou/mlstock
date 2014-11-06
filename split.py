#!/usr/bin/env python
import sys
line = sys.argv[1]
items = line.split(sys.argv[2])
for item in items:
    if not item:
        continue
    print item
