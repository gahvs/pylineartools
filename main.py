from pylineartools import Matrix 

m = Matrix(5, 5)
m.randomize(integer=True)

for line in m.numbers(): print(line)
print()

identity = m.identity()
for line in identity.numbers(): print(line)
print()

product = Matrix.product(m, identity)
for line in product.numbers(): print(line)
print()
