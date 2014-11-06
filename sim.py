#!/usr/bin/env python
import pandas as pd
from sklearn.metrics import pairwise_distances
from sklearn.preprocessing import scale
import sys


name = sys.argv[1]
df = pd.read_csv(name, index_col=0,  header=None)
name = df.index
df = scale(df)
dist_out = pairwise_distances(df, metric="cosine")
s = pd.DataFrame(dist_out, index=name, columns=name)
for i in name:
    rs = ''
    rs += (str(i)+':')
    sim_rs = s.ix[i]
    sim_rs = sim_rs.order()
    neighour = sim_rs[-20:]
    for k in neighour.index:
        rs += (str(k) + ',')
    print rs
