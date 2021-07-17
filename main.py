from pylineartools import Matrix, MatrixComponent

a = Matrix(rows=3, cols=3)
a.randomize(integer=True)
print(a.matrix())
