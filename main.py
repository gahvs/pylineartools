from pylineartools import Matrix, MatrixComponent

a = Matrix()
b = Matrix()

a.add(MatrixComponent(1, 1, 2))
a.add(MatrixComponent(1, 2, 3))
a.add(MatrixComponent(1, 3, 1))
a.add(MatrixComponent(2, 1, -1))
a.add(MatrixComponent(2, 2, 0))
a.add(MatrixComponent(2, 3, 2))

b.add(MatrixComponent(1, 1, 1))
b.add(MatrixComponent(1, 2, -2))
b.add(MatrixComponent(2, 1, 0))
b.add(MatrixComponent(2, 2, 5))
b.add(MatrixComponent(3, 1, 4))
b.add(MatrixComponent(3, 2, 1))

mProduct = Matrix.product(a, b)
print(mProduct.matrix())