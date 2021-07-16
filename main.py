from pylineartools.vector import Vector, VectorComponent

v1 = Vector()
v1.add(component=VectorComponent(index=1, number=10))
v1.add(component=VectorComponent(index=2, number=20))
v1.add(component=VectorComponent(index=3, number=30))

v2 = Vector.copy(vector=v1)

vSum = Vector.sum(v1, v2)
print(v1.vector())
print(v2.vector())
print(vSum.vector())