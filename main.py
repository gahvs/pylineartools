from pylineartools import *

m = Matrix.toMatrix(Vector([1, 2, 3, 4, 5]))

for line in m.values():
    print(line)