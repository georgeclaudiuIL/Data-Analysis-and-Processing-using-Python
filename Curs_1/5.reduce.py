
from functools import reduce


culori = ["alb", "rosu", "negru", "verde"]

print(reduce(lambda x, y: x if len(x)<len(y) else y, culori))

