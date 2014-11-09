import numpy as np
from sklearn.datasets import load_digits
from sklearn.preprocessing import scale

np.random.seed(4)
digits = load_digits()
data = scale(digits.data)
print data[][1]
