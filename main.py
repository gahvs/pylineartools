from pylineartools import Matrix

m = Matrix(2, 4)
m.randomize(integer=True)

for line in m.numbers(): print(line)
print()

transposed = m.transpose()
for line in transposed.numbers(): print(line)
print()
