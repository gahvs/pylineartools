# pylineartools
Biblioteca em python para problemas de Álgebra Linear.

## pylineartools v0.2

Biblioteca escrita em Python para dar suporte a solução de problemas de Álgebra Linear. A biblioteca implementa classes e funcionalidades que permitem a solução direta de problemas, mas que também podem dar suporte e facilitar a construção da sua própria solução, quando isto lhe for conveniente.

Além de uma larga aplicação em áreas da matématica, ela pode ser bastante útil em áreas da computação, como por exemplo, na construção de algoritmos de Redes Neurais Artificiais ou em Geometria Computacional, que fazem diversos cálculos e manipulações envolvendo matrizes e vetores.

###  Vetores e Matrizes
A biblioteca fornece Classes que implementam conceitos elementares de Álgebra Linear, em especial, relacionados a Matrizes e Vetores. Embora um vetor não seja nada além de uma matriz unidimensional, aqui eles são definidos de forma separada.

#### Vetores
Um **vetor** é uma função que leva um conjunto finito arbitrário de índices (domínio) no conjunto dos números reais (imagem), se tal conjunto de índices de um vetor **x** é **N**, dizemos que **x** está definido **sobre** N. Logo, se **x** é um vetor definido sobre **N** e **n** é um elemento de **N** então **x [n]** denota o **componente** n de **x**, ou seja, o valor da função x em n.

#### Matrizes
Uma **matriz** é uma função que leva o produto cartesiano de dois conjuntos finitos no conjunto dos números reais. Se uma matriz **M** tem domínio *L x N*, dizemos que *L* é o conjunto de **índices de linha** e *N* é o conjunto de **índices de coluna** de M. Dizemos também que M é uma matriz definida sobre *L x N.

*Seja para vetores ou seja para matrizes, convém não presumir nenhuma relação de ordem sobre os conjuntos de índices.*

### Instalação e importação

A biblioteca está disponível via pip através do comando:

```python
    pip install pylineartools
```

Importação das classes *Matrix* e *Vector* para trabalhar, respectivamente, com matrizes e vetores:


```python
from pylineartools import Vector
from pylineartools import Matrix
```

### Vector

Para trabalhar com a classe Vector uma forma fácil de iniciar um vetor é passar para o método constrututor os valores que queremos no nosso vetor.
Os valores podem ser descritos literalmente, passsados como uma lista e até como uma mesclagem das duas formas:


```python
v1 = Vector(1, 2.5, 3.5, 4.5, 5)
v2 = Vector([x for x in range(6, 11)])
v3 = Vector(1, 2, 3, [x for x in range(4, 9)], 9, 10)
```

Uma vez criados, podemos ver o vetor completo (índices e valores) ou só os seus valores através dos métodos vector() e values(), respectivamente.


```python
v1.vector(), v2.vector(), v3.vector()
```




    ({1: 1, 2: 2.5, 3: 3.5, 4: 4.5, 5: 5},
     {1: 6, 2: 7, 3: 8, 4: 9, 5: 10},
     {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 10: 9, 11: 10})




```python
v1.values(), v2.values(), v3.values()
```




    ((1, 2.5, 3.5, 4.5, 5), (6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))



Para adicionar novos componentes em um vetor, usamos o método add(). Esse método exige que o argumento passado seja um objeto da classe VectorComponent. 

Veja no exemplo abaixo um vetor em branco criado para então tendo seus componentes adicionados. Neste exemplo introduzimos o método indexes(), que retorna a lista de índices do vetor.


```python
from pylineartools import VectorComponent
v4 = Vector()

#adding components
v4.add(component=VectorComponent(index=1, value=1))
v4.add(component=VectorComponent(index=999, value=2))
v4.add(component=VectorComponent(index=-999, value=3))

v4.indexes(), v4.values(), v4.vector()
```




    ((1, 999, -999), (1, 2, 3), {1: 1, 999: 2, -999: 3})



Para modificar um component existente use change()


```python
v4.change(index=-999, value=0.00000001)
v4.values()
```




    (1, 2, 1e-08)


