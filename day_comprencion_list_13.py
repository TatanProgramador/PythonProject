# una vía
from day_list_05 import new_lst

language = 'Python'
lst = list(language)
print(type(lst))
print(lst)
#Segunda vía: comprensión de listas
lst = [i for i in language]
print(type(lst))
print(lst)

# Generar una lista de numeros

numbers = [i for i in range(10)]
print(numbers)

#Es posible realizar operaciones matemáticas durante la iteración.

# square = [i * i for i in range(11)]
# print(square)
square = []
for i in range(11):
    result = i * i
    square.append(result)
print(square)

# También es posible hacer una lista de tuplas
numbers = [(i, i * i) for i in range(10)]
print(numbers)

numbers = []

for i in range(10):
    product = i * i
    pair = (i, product)
    numbers.append(pair)

print(numbers)

#Generando numeros pares
even_numbers = [i for i in range(21) if i % 2 == 0]
print('Números pares: ',even_numbers)

#Generando numeros impares
odd_numbers = [i for i in range(21) if i % 2 != 0]
print('Números impares: ', odd_numbers)

# Números de filtro: filtremos los números pares positivos de la lista a continuación

numbers = [0 , 1, 2, 3, 4, 5, 6, 12, 22, 45, 32, -2, -4, -1, 0]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print('Estos son los numeros positivos pares: ', positive_even_numbers)

# Aplanamiento de un array bidimencional(matriz)
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12, 13, 14, 15]]
flattened_list = [number for row in list_of_lists for number in row]
print(list_of_lists)
print(flattened_list)

# Creación Lambda: Una función lambda es una función anónima pequeña sin nombre. Puede aceptar cualquier número de argumentos, pero solo puede tener una expresión. Es similar
# a las funciones anónimas de JavaScrip. Las necesitamos cuando queremos escribir una funcion anónima dentro de otra
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(param1=5, param2=10, param3=20))

#Funcion con nombre
def add_two_numbers(a, b):
    return a + b

print(add_two_numbers(2, 3))

#Cambiemos la funcion anterir a lambda
add_two_numbers = lambda a, b: a + b
print(add_two_numbers(2, 3))

# Funcion lambda autoinvocable
print((lambda a, b: a + b)(2, 2) )# 5 - es necesario encapsularlo en print() para ver el resultado en la consola

square = lambda x : x ** 2
print(square(5))
cube = lambda x : x ** 3
print(cube(5))
multiple_variabes = lambda a, b, c : a**b + b - 3*c
print(multiple_variabes(5, 10, 15))

# Usando una función lambda dentro de otra funcion

def power(x):
    return lambda n : x ** n
cube = power(2)(3) # La función power ahora necesita 2 argumentos para ejecutarse, en corchetes redondeados separados
print(cube)
two_power_of_five = power(2)(5)
print(two_power_of_five)

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

numbers_negativos = [i for i in numbers if i < 0 or i == 0]
print(numbers_negativos)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

list_matriz = [numbers for row in list_of_lists for numbers in row]
print(list_matriz)

list_tuples = [(n , 1, n ** 2, n ** 3, n ** 4, n ** 5) for n in range(10)]
print(list_tuples)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = [[country.upper(), country [:3].upper(), capital.upper()]
          for row in countries
          for country, capital in row]
print(output)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [{'country':country.upper(), 'city':capital.upper()}
          for row in countries
          for country, capital in row]
print(output)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

output = [first + " " + last for row in names for first, last in row]

print(output)


slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

intercept = lambda x1, y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1

m = slope(2, 3, 5, 11)     # pendiente
b = intercept(2, 3, 5, 11) # intersección con el eje y

print(m, b)







