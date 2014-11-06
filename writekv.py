#!/usr/bin/env python
import memcache
import sys

s = memcache.Client(["127.0.0.1:11211"])
for line in sys.stdin:
    line = line.strip()
    items = line.split(':')
    key = items[0]
    value = items[1]
    s.set(key, value)
