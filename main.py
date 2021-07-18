from pylineartools import Vector

v = Vector(1, 2, 3, [x for x in range(4, 9)], 9, 10)
print(v.numbers())