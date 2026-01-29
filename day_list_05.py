
import copy
from itertools import count

#
# lst = list()
# lst.append('A')
# lst.append('B')
# lst.append('C')
# lst.append('D')
#
# lst.extend(['E', 'F', 'J'])
#
# print(type(lst))
# print(lst)
# print(len(lst))
#
# lst = ['Bananas','Manzanas']
# print(type(lst))
# print(lst)
# print(len(lst))
#
# fruits = ['apple', 'banana', 'orange']
# vegetales = ['tomato', 'pimenton', 'cebolla']
# animal_products = ['milk', 'meat', 'butter', 'yoghurt']
# countries = ['Colombia', 'USA', 'Panama', 'Suiza']
#
# print(f'Frutas en lista: {fruits}')
# print(f'La cantidad de las frutas es de: {len(fruits)}')
# print(f'El primer elemento de la lsita es de: {fruits [0]}')
# print(f'Vegetales en la lista: {vegetales}')
# vegetales.append('Pepino')
# print(vegetales)
# print(f'El ultimo elemento de la lissta es de: {vegetales[-1]}')
#
# lst = ['Asabeneh', 250, True, {'Country': 'Colombia', 'Country': 'USA'}]
#
# lst2 = {'Country': 'Colombia', 'Country': 'USA'}
# print(lst)
# print(len(lst))
# print(lst[0])
# print(lst[1])
# print(lst[2])
# print(lst[3])
# print(lst2['Country'])
#
# fruits = ['banana', 'orange', 'mango', 'lemon']
# first_fruit = fruits[0] # we are accessing the first item using its index
# print(first_fruit)      # banana
# second_fruit = fruits[1]
# print(second_fruit)     # orange
# last_fruit = fruits[3]
# print(last_fruit) # lemon
# # Last index
# last_index = len(fruits) - 1
# print(last_index)
# last_fruit = fruits[last_index]
# print(last_index)
# print(last_fruit)
#
# lst = ['item1', 'item2', 'item3', 'item4', 'item5']
# first_item, second_item, third_item, *rest = lst
# print(first_item)
# print(second_item)
# print(third_item)
# print(rest)
#
# fruits = ['banana', 'orange', 'mango', 'lemon', 'mandarin', 'pera']
# first_fruit, second_fruit, third_fruit, *rest = fruits
# print(first_fruit)
# print(second_fruit)
# print(third_fruit)
# print(rest)
#
# print(type(rest))
#
# first, second, third, *rest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(rest)
# print(type(rest))
# print(first)
# print(second)
# print(third)
#
# countries = ['Colombia', 'USA', 'Panama', 'Suiza', 'Germany', 'Esdtonia', 'Uruguay']
# print(countries)
# co, us, pa, *conjunto_pais, es = countries
# print(co) # Colombia
# print(us) # USA
# print(pa) # Panama
# print(es) # Uruguay
# print(conjunto_pais) # Suiza, Germany # El * en la variable quiere decir que va a tomar los elementos que aún no estan asignados
#
#
# fruits = ['banana', 'orange', 'mango', 'lemon']
# all_fruits = fruits[0:4] # it returns all the fruits
# # this will also give the same result as the one above
# print(all_fruits)
# all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
# print(all_fruits)
# orange_and_mango = fruits[1:3] # it does not include the first index
# print(orange_and_mango)
# orange_mango_lemon = fruits[1:]
# orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']


fruits_example = ['Banana', 'Orange', 'Mango', 'Lemon', 'Kiwi', 'Papaya']
print(fruits_example [0:3:1]) # Banana, Orange, Mango
print(fruits_example [0:4:1]) # Banana, Orange, Mango, Lemon
print(fruits_example[::2])  # Banana, Mango, Kiwi
print(fruits_example[0:4:1]) # Banana, Orange, Mango, Lemon
print(fruits_example[2:6:1]) # Mango, Lemon, Kiwi, Papaya
print(fruits_example[1:5:2]) # Orange, Lemon
print(fruits_example[-3:6:1]) # Lemon, Kiki, Papaya start equivale a: len(fruit) = (-3) = 6 - 3 = 3
print(fruits_example[0:-2:1]) # Banana, Orange, Mango, Lemon stop equivale a 6 - 2 = 4
print(fruits_example[5::-1]) # Papaya, Kiwi, Lemon, Mango, Orange, Banana # El -1 me indica que son todos los elementos de para atras
print(fruits_example[4:0:-1]) # Kiwi, Lemon, Mango, Orange
print(fruits_example[3:100:1]) # Lemon, Kiwi, Papaya  Python limita al final de la lista

# Si start no esta empieza desde el final
# Si stop no esta llegara hasta el final
# El step es el que me dice la iteracion entre la lista si es negativa empieza de para atras

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # banana, orange, mango, lemon
print(all_fruits)
# it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # banana, orange, mango, lemon
# if we don't set where to stop it takes all the rest
print(all_fruits)
orange_and_mango = fruits[1:3] # orange, mango
print(orange_and_mango)
# it does not include the first index
orange_mango_lemon = fruits[1:]# orange, mango, lemon
print(orange_mango_lemon)
orange_and_lemon = fruits[::2] #
print(orange_and_lemon)
# here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']


fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # Banana
print(all_fruits)# it returns all the fruits
# Lemon, Kiki, Papaya start equivale a: len(fruit) = (-3) = 6 - 3 = 3
# len(fruit) - (-3) = 4 - 3 = 1
orange_and_mango = fruits[-3:-1] #orange, mango
print(orange_and_mango)
# it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # orange , mango, lemon
# this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # lemon, mango, orange, banana
print(reverse_fruits)
# a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']


frruits = ['banana', 'orange', 'mango', 'lemon']
fruits [0] = 'avocado'
print(fruits)
fruits [1] = 'manzana'
print(fruits)
last_index_fruits = len(fruits)-1
print(last_index_fruits)
fruits[last_index_fruits] = 'pera'
print(fruits)

fruits = 'banana', 'orange', 'mango', 'lemon'
does_exist = 'orange' in fruits
print(does_exist)

# lst = list()
# lst.append(item)

fruits = ['banana', 'orange', 'mango', 'lemon', []]
fruits.append('lemon')
print(fruits)
fruits.insert(0, 'lemon')
print(fruits)
fruits.remove([])
print(fruits)
fruits.remove('lemon')
print(fruits)
fruits.pop(0)
print(fruits)

#La diferencia entre .remove('banana') .pop(0)  es en su contenido, que con remove me va a eliminar de la lista es el valor y debe estar escrito talcual como en la lista creada
# y con .pop(0) se elimina es el indice del contenido de la lista

del fruits[1]
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lemon']
print(fruits)
del fruits[0] # elimina el ityem 0 = banana
print(fruits) # orange, mango, lemon, kiwi, lemon
del fruits[1]# elimina el item 1 = mango
print(fruits) # orange, lemon, kiwi, lemon
del fruits[1:3]# star, stop, step empieza en orange lemon es el segundo y el tercero no cuenta por que es el star
print(fruits)

lst = ['item 1', 'item 2']
print(lst)
print(type(lst))
lst.clear()
print(lst)
print(type(lst)) # El metodo .clear me vacia toda la lista

lst = ['item 1', 'item 2', 'item 3', []]
print(lst)
copy_lst = lst[:]
print(copy_lst)
copy_lst = lst.copy()
print(copy_lst)
new_lst = copy.deepcopy(lst)
print(new_lst)

lst = [[1, 2], [3, 4]]
copy_shallow = lst.copy()
copy_deep = copy.deepcopy(lst)

copy_shallow  [0][0] = 99
copy_deep  [1][1] = 88
print('Original', lst)
print('Shallow' , copy_shallow)
print('Deep ',copy_deep)

#Unir listas

lst_1 = [1, 2, 3, 4]
lst_2 = ['Hola', 'Mundo']

lst_3 = lst_1 + lst_2
print(lst_3)

lst_1.extend(lst_2)
print(lst_1)

numbers = [1, 2, 3, 4, 1, 'Hola', ()]
print(numbers.count(1))
print(numbers.count(())) # Devuelve la cantidad de veces que esta un elemneto dentro de la lista

print(numbers.index(3))
print(numbers.index('Hola'))
print(numbers.index(())) # Devueve el indixe en el que se encuientra dicho elemento

numbers.reverse()
print(numbers) # El metodo reverse me revierte toda la lista y me la muestra revertida

numbers = [8, 9 , 3, 3, 5,6 ,7 ,1 ,2, 4]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

fruits = sorted(fruits)
print(fruits)

fruits = sorted(fruits, reverse=True)
print(fruits) # El metodo sort me ordena primordialmente de forma ascendente de menor a mayor y modifica la misma lista y sorted me crea otra lista aparte de la tomada
# Y para que me tome de forma descendente debo igualar reverse a True

lst = []
lst_2 = list()
print(lst)
print(lst_2)
print(type(lst))
print(type(lst_2))
lst_element = [1, 'Hola mundo', (), [], 1.4]
print(len(lst_element))
print(lst_element [0]) # Primer elemento
print(lst_element [2:3]) #Elemnto del medio
print(lst_element [-1]) # Ultimo elemneto 

mixed_data_type = ['Edilson', '20', 1.80, 'Soltero', 'Cra 8 9 -42']
it_companies = ['Facebook', 'google', 'Microsoft', 'Apple', 'IBM,', 'Oracle', 'Amazon','Cocacola' ]
print(it_companies)
print(len(it_companies))
result = it_companies [0:2] + it_companies[-1:]
print(result)

it_companies.remove(it_companies[0])
print(it_companies)

it_companies.append('Tesla')
print(it_companies)

#posicion = 3
posicion = len(it_companies) // 2
result = it_companies [0]
print(posicion)
it_companies.insert(posicion, 'AWS')

print(it_companies)

it_companies [0] = it_companies[0].upper()

print(it_companies)

cadena = '#;    '

it_companies_cadena = cadena .join(it_companies)
print(it_companies_cadena)

cadena = 'Tesla'

print(cadena in it_companies)

it_companies.sort()
print(it_companies)

it_companies.sort(reverse=True)
print(it_companies)

result = it_companies [3:7]
print(result, 'Estas son las tres primeras empresas separadas', it_companies [0], it_companies [1], it_companies [2])

del it_companies[-3:]



it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

posicion = len(it_companies) // 2

mitad_1 = posicion
mitad_2 = posicion - 1

print(mitad_1, mitad_2)
print(it_companies)

if len(it_companies) % 2 != 0:
    del it_companies[mitad_1]
    print('Es con una condición impar')
else:
    del it_companies[mitad_1]
    del it_companies[mitad_2]
    print('Es una codicion par')
print(it_companies)

it_companies.remove(it_companies[0])

print(it_companies)


posicion = len(it_companies) // 2

par = posicion
impar = posicion - 1

if len(it_companies) % 2 != 0:
    del it_companies[par]
    print('Es con una condicion impar')
else:
    del it_companies[par]
    del it_companies[impar]




