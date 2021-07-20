from pylineartools import Matrix, MatrixComponent

m = Matrix()

m.add(MatrixComponent(1, 1, 1))
m.add(MatrixComponent(1, 2, 2))
m.add(MatrixComponent(2, 1, 3))
m.add(MatrixComponent(2, 2, 4))

mapping = m.map(function=lambda c: c ** 2)

print(m.values())
print(mapping.values())
