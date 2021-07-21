from pylineartools import *

v = Vector(1, 2, 3, 4, 5)

print(v.map(lambda x: x**2).values())