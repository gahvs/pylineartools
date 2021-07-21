from pylineartools import Matrix, MatrixComponent

def inline(m):
    for line in m.values():
        print(line)
    print()

m = Matrix()

m.add(MatrixComponent(1, 1, 1))
m.add(MatrixComponent(1, 2, 2))
m.add(MatrixComponent(2, 1, 3))
m.add(MatrixComponent(2, 2, 4))
m2 = m.copy()

inline(m)
inline(m2)
inline(Matrix.hadamard(m, m2))
inline(Matrix.sum(m, m2))
