import os
import time
prefix = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
for i in range(100000):
    i = str(i).zfill(6)
    print i
    addr = prefix%i
    os.system('wget %s -O data/%s.csv --timeout=3'%(addr, i))
    time.sleep(0.1)


