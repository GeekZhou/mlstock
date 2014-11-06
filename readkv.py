#!/usr/bin/env python
import memcache
import sys

s = memcache.Client(["127.0.0.1:11211"])
print s.get(sys.argv[1])

