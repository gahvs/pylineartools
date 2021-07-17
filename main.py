from random import random
from pylineartools import vector
from pylineartools.vector import VectorComponent
from pylineartools import Vector, VectorComponent

v = Vector(1, 2, 3, [x for x in range(4, 9)], 9, 10)
print(v.numbers())