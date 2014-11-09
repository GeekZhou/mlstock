#!/usr/bin/env python
import memcache
import sys

s = memcache.Client(["127.0.0.1:11211"])
id = sys.argv[1]
print s.get(id)

