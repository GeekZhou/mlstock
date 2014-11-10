#!/usr/bin/env python
import sys
for line in sys.stdin:
    line = line.strip()
    print line.zfill(6)
