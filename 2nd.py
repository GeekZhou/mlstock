#!/usr/bin/env python
import sys
lines = sys.stdin.readlines()
self = lines[0]
sid, sname, srat = self.split(',')
pair = lines[1]
pid, pname, prat = pair.split(',')
delta = float(srat.replace('%','')) - float(prat.replace('%','') )
if delta > 0.4 :
    print sid, sname, srat, pid, pname, prat, delta 
