#!/usr/bin/env python
import pandas as pd
from sklearn.metrics import pairwise_distances
from sklearn.preprocessing import scale
import sys

name = sys.argv[1]
num = int(sys.argv[2])
df = pd.read_csv(name,sep=',',  index_col=0,  header=None)
dist_out = pairwise_distances(df, metric="cosine")
name = df.index
s = pd.DataFrame(dist_out, index=name, columns=name)

for i in name:
    rs = ''
    rs += (str(i)+':')
    sim_rs = s.ix[i]
    sim_rs = sim_rs.order(ascending=False)
    neighour = sim_rs[:num]
    for k in neighour.keys():
        rs += (str(k) + ',')
    print rs
