#!/usr/bin/env python
import pandas as pd
from sklearn.metrics import pairwise_distances
from sklearn.preprocessing import scale
import sys


name = sys.argv[1]
df = pd.read_csv(name, index_col=0,  header=None)
array = scale(df)
for row in array:
    print row
