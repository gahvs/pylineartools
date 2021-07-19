from pylineartools import Matrix

m = Matrix(2, 4)
m.randomize(integer=True)
print(m.matrix())
c = m.copy()
print(c.matrix())