

st = set()

## La diferencia entre list y set es que list en algo ordenado y que sigue una secuencia ordenada en la que se van agregando datos o se van eliminando ,
## en ves de set que es algo lo cual esta desordenado y un indixe no siempre va a ser el mismo ya que en el momento de guardarse y mostrarse no siempre
## es esa misma posicion
lst = ['item1', 'item2', 'item3', 'item4']
lst.append('item5')
print(lst)
lst.remove('item5')
del lst[3]
print(lst)

print(lst)

st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
print(st)
st.remove('item5')
print(st)
st.update(['item6', 'item7'])
print('Este es el ejemplo',st)

print('Este contenido se encuentra en el set item1', 'item1' in st)

fruits = {'apple', 'banana', 'orange'}
print(type(fruits))
vegetables = {'tomato', 'pimenton', 'cebolla'}
print(type(vegetables))
fruits.update(vegetables)
print(fruits)
print(type(fruits))


if 'banana' in fruits:
    fruits.remove('banana')
    ##print(fruits)
    print('Esta es el sed con las modificaciones', fruits)
else:
    print('Esa fruta no se encuentra en el set fruits')

print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()  # removes a random item from the set
print(fruits)
fruits.clear()
print(fruits)

lst = ['banana', 'orange', 'mango', 'lemon']
st = set(lst)
print(type(st))
print(st)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}
print(whole_numbers)
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}

## issubset quiere decir que todos los elementos de st1 estan en st2
## issuperset st1 contiene todos los elementos de st2
st1 = {'item1', 'item2', 'item3', 'item4', 'item9'}
st2 = {'item1', 'item2', 'item3', 'item4'}
print(st1.issubset(st2))## False
print(st2.issubset(st1)) ##True
print(st1.issuperset(st2))##True
print(st2.issuperset(st1))##False


fruits1 = {'apple', 'banana', 'fresa', 'mango', 'orange'}
fruits2 = {'apple', 'banana', 'orange', 'fresa', 'pera', 'mango'}
print(fruits1.issubset(fruits2))## True
print(fruits2.issubset(fruits1)) ## False
print(fruits1.issuperset(fruits2))## False
print(fruits2.issuperset(fruits1)) ## True

nums1 = {1, 2, 3 }
nums2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(nums1.issubset(nums2))## True
print(nums2.issubset(nums1))## False
print(nums1.issuperset(nums2))## False
print(nums2.issuperset(nums1))## True

permisos_usuario = {'leer', 'escribir', 'subir_archivos'}
permisos_admin = {'leer', 'escribir', 'subir_archivos', 'eliminar', 'configurar'}

print(permisos_usuario.issubset(permisos_admin)) ##True
print(permisos_admin.issubset(permisos_usuario)) ## False
print(permisos_usuario.issuperset(permisos_admin))## False
print(permisos_admin.issuperset(permisos_usuario)) ## True

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.difference(st1))
print(st1.difference(st2))

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers) )# {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.difference(dragon))     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
print(dragon.difference(python))    # {'d', 'r', 'a', 'g'}

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6'}
print(st1.symmetric_difference(st2)) ## item1 item4

python.symmetric_difference(dragon) ##p y t d r a g

print(python.isdisjoint(dragon))
print(dragon.isdisjoint(python))
print(st1.isdisjoint(st2))

##Ejercicios: Nivel 1
##Encuentra la longitud del conjunto it_companies
##Añadir 'Twitter' a it_companies
##Insertar varias empresas de TI a la vez en el conjunto it_companies
##Eliminar una de las empresas del conjunto it_companies
##¿Cuál es la diferencia entre eliminar y descartar?

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twiter')
print(it_companies)

it_companies.update(['Youtube', 'TikTok'])
print(it_companies)

it_companies.remove('Google')
it_companies.discard('Apple')
print(it_companies)

##La diferencia entre remove y discard es que en el remove elimina el elemnto si existe y lanza un key error
# si no eviste y en ves del discard no sale el error y sigue adelante asi no enccuentre el elemento para eliminarlo.

print(A.union(B))
print(A.intersection(B))
print(A.issubset(B)) ## 19, 22, 24, 20, 25, 26
print(A.isdisjoint(B))
print(A.union(B)) or print(B.union(A))
print(A.symmetric_difference(B))
# del A
# del B

print(age)
con_age = age
con_age = set(age)
print(type(con_age))
print(con_age)

print(len(age))
print(len(con_age))

if len(age) >= len(con_age) :
    print('La lista es mayor que el conjunto')

elif len(con_age) >= len(age) :
    print('El conjunto es mayor que el conjunto')

else :
    print('No entra')


# Cadena (string): Es un tipo de dato que permite almacenar una secuencia de caracteres.
# Puede contener letras, números, símbolos y espacios, siempre que estén entre comillas
# simples, dobles o triples. Las cadenas son inmutables.
#
# Lista: Es una estructura de datos que permite almacenar múltiples elementos de distintos
# tipos. Es una colección ordenada y mutable, lo que significa que sus elementos pueden
# modificarse, eliminarse o agregarse. Cada elemento tiene un índice y se define usando
# corchetes [].
#
# Tupla: Es una estructura de datos similar a la lista, ya que permite almacenar múltiples
# elementos de distintos tipos y mantiene el orden. La diferencia principal es que es
# inmutable, es decir, no se puede modificar después de creada. Se define usando paréntesis ().
#
# Conjunto (set): Es una estructura de datos que almacena elementos únicos, sin orden y sin
# índices. No permite valores duplicados y se define usando llaves {} o mediante la función
# set().

palabra1 = 'ínspirar'
palabra2 = 'enseñar'

letras_repetidas = set()

for letras in palabra1:
    if letras in palabra2:
        letras_repetidas.add(letras)

print('Letras que se repiten',letras_repetidas)
print('Las letras que se estan repitiendo son: ',len(letras_repetidas))


