from pylineartools import Matrix

m = Matrix(3, 3)
m.randomize(integer=True)
print(m.numbers())