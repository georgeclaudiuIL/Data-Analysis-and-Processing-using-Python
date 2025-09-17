
# Este bisect daca:
# 1. Este divizibil cu 400
# 2. Este divizibil cu 4, dar nu cu 100

import numpy as np


startDate = 1899
endDate = 2025

array = np.arange(startDate, endDate+1)
# print(array)

print(array[(array % 400 == 0) | ((array % 4 == 0) & (array % 100 != 0))])
