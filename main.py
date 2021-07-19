from pylineartools import Matrix 

m = Matrix(5, 5)
m.randomize(integer=True)

for line in m.numbers(): print(line)
print()

transposed = m.transpose()
for line in transposed.numbers(): print(line)
print()