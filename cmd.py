#!/usr/bin/env python
import sys
import os
cmd = sys.argv[1]

for line in sys.stdin:
    line = line.strip()
    ecmd =cmd.replace('$1', line)
    print ecmd
    os.system(ecmd)


