# from itertools import count
#
# from day_variables_builtin_functions_02 import first_name
#
#
# def generate_full_name ():
#     firt_name = 'Edilson'
#     last_name = 'Fabian'
#     space = ' '
#     full_name = f'{firt_name}{space} {last_name} '
#     return full_name
# print(generate_full_name())
#
# def add_two_numbers():
#     num_one = 2
#     num_two = 3
#     total = num_one + num_two
#     return total
# print(add_two_numbers())
#
# # funtions wich parameter
#
# def greeting (name):
#     message = name, (', welcome to Python for Everyone!')
#     return message
# print(greeting('Edilson'))
#
# def add_ten(num):
#     ten = 10
#     return ten + num
# print(add_ten(90))
#
# def scuare_number (x):
#     return x * x
# print(scuare_number(100))
#
# def area_of_circle (r):
#     pi = 3.14
#     area = pi * (r ** 2)
#     return area
# print(area_of_circle(100))
#
# #n = int(input('Ingrese el numero n para dicha operacion'))
#
# def sum_of_numbers(n):
#     total = 0
#     for i in range(n+1):
#         total+=i
#     return total # 1, ,2 3, 4,5,6,7,8,9,10,11,12,13,14,15
# print(sum_of_numbers(10)) # 120
#
# def print_fullname(firstname, lastname):
#     space = ' '
#     full_name = firstname  + space + lastname
#     print(full_name)
# print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh')
#
# def print_full_name(first_name, last_name):
#     space = ' '
#     full_name = first_name + space + last_name
#     print(full_name)
# print_full_name(first_name = 'Edilson', last_name ='Gomez')
#
# def add_two_numbers(num1, num2):
#     total = num1 + num2
#     return total
# print(add_two_numbers(10, 20))
#
# def add_two_numbers(num1, num2):
#     total = num1 + num2
#     return total
# print(add_two_numbers(num1 = 2, num2 = 3))
#
# def calcutator_age(añoNacimiento, añoActual):
#     age = añoActual - añoNacimiento
#     return age
# print('Age:',calcutator_age(añoNacimiento = 2005, añoActual = 2025))
#
# #num = int(input('Enter a number: '))
#
# def isEven (num):
#     if num % 2 == 0:
#         print('El número es par', num)
#         return True
#     else:
#         print('El número es impar', num)
#         return False
# print(isEven(12))
#
# #num = int(input('Ingresa un numero: '))
#
# def find_even_and_odd(num):
#     even = []
#     odd = []
#
#     for i in range(num + 1):
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#
#     return even, odd
#
# pares, impares = find_even_and_odd(21)
# print("Pares:", pares)
# print("Impares:", impares)
#
#
# def greetings (name = 'Edilson'):
#     message = name, (', welcome to Python for Everyone!')
#     return message
# print(greetings())
# print(greetings('Fabian'))
#
#
# def generate_full_name (first_name = 'Edilson', last_name = 'Gomez'):
#     space = ' '
#     full_name = first_name + space + last_name
#     return full_name
# print(generate_full_name())
# print(generate_full_name(first_name = 'Fabian',last_name='Torrado'))
#
# def calculate_age (fechaNacimiento , fechaActual= 2025):
#     age = fechaActual - fechaNacimiento
#     return age
# print(calculate_age(fechaNacimiento=2005))
# print(calculate_age(fechaNacimiento=2025))
#
# def weight_of_object (mass, gravity = 9.81):
#     weigh = str(mass * gravity) + 'N'
#     print(type(weigh))
#     return weigh
# print('Peso de un objeto en Newton: ',weight_of_object(mass = 100))
# print('Peso de un objeto en Newton: ',weight_of_object(mass = 100, gravity = 1.62))
#
# def sum_all_nums (*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
# print(sum_all_nums(100, 39,34))
#
# def generate_groups(team, *args):
#     print(team)
#     for i in args:
#         print(i)
#
# generate_groups('Team-1: ', 'Edilson', 'Danna','Dilia', 'Laura', 'Tatan' )
# generate_groups('Team-2: ' , 'Carlos', 'Sofia','Ester', 'Camila', 'Catalina' )
#
# #Define una función que toma dos argumentos: 'nombre' y 'ubicación'
# def greet(name, location):
#     # Imprima un mensaje de saludo utilizando los argumentos proporcionados
#     print("Hi there", name, "how is the weather in", location)
#
# # Llamar a la función usando argumentos de palabras clave
# greet(name="Alice", location="New York")
# # Salida: Hola Alice, ¿cómo está el clima en Nueva York?
#
# # Crea un diccionario con claves que coincidan con los nombres de los parámetros de la función
# my_dict = {"name": "Alice", "location": "New York"}
#
# # Llamar a la función usiunpackingng diccionario
# greet(**my_dict)
# # El operador ** descomprime el diccionario, pasando sus pares clave-valor
# # como argumentos de palabra clave a la función.
# # Salida: Hola Alice, ¿cómo está el clima en Nueva York?
#
#
# def arbitrary_named_args(**args):
#     print("I received an arbitrary number of arguments, totaling", len(args))
#     print("They are provided as a dictionary in my function:", type(args))
#     print("Let's print them:")
#     for k, v in args.items():
#         print(" * key:", k, "value:", v)
# print(arbitrary_named_args(**{'a': 1, 'b': 2, 'c': 3}))
#
# #You can pass functions around as parameters
# def square_number (n):
#     return n ** n
# def do_something(f, x):
#     return f(x)
# print(do_something(square_number, 3)) # 9
#
#
#
from zoneinfo import reset_tzpath

from day_list_05 import new_lst, fruits_example
from operadores_logicos import lenguaje

# num1 = int(input("Ingrese el primer número de la operación "))
# num2 = int (input('ingrese el segundo número de la operación'))
# def add_two_numbers (num1, num2):
#     return num1 + num2
#
# print('La sema de los números ' , num1 ,'y ', num2 , 'es de: ', add_two_numbers(num1, num2))


# radius = int(input('Ingrese el radius '))
#
# def area_circle(radius):
#     pi = 3.14
#     area = pi * radius * radius
#     return area
# print(area_circle(radius))

# def add_all_nums(*args):
#     if not all(isinstance(num, (int, float)) for num in args):
#         return 'Error: todos los elementos deben ser numericos'
#
#     total = sum(args)
#     return f'El resultado es: {total}'
#
# print('Ejemplo con datos numericos: ',add_all_nums(1, 2, 3))
# print('Ejemplo con datos no numericos: ',add_all_nums(1, 2, 'Numeros', 4))
#
# celsius = float(input('Celsius: '))
#
# def convert_celsius_to_fahrenheit(celsius):
#     return celsius * 9 / 5 + 32
# print('La conversion de ' ,celsius ,'grados celsius a farengei es de: ' , convert_celsius_to_fahrenheit(celsius))

#
# primavera = ['marzo', 'abril', 'mayo']
# verano = ['junio', 'julio', 'agosto']
# otoño = ['septiembre', 'octubre', 'noviembre']
# invierno = ['diciembre', 'enero', 'febrero']
#
# def check_season(mes):
#
#     mes = mes.lower()
#
#     if mes in primavera:
#         return 'Primavera'
#     elif mes in verano:
#         return 'Verano'
#     elif mes in invierno:
#         return 'Invierno'
#     elif mes in otoño:
#         return 'Otoño'
#     else:
#         return 'Mes no valido'
#
# print(check_season("Marzo"))
# print(check_season("AGOSTO"))
# print(check_season("febrero"))
# print(check_season("banana"))


#
# punt_one_x = int(input("Punt one X: "))
# punt_one_y = int(input("Punt one Y: "))
# punt_two_x = int(input("Punt two X: "))
# punt_two_y = int(input("Punt two Y: "))
#
# y = [punt_one_y, punt_two_y]
# x = [punt_one_x, punt_two_x]
# print(y)
# print(x)
#
# def calculate_spole():
#     print("Formula de la pendiente entre dos puntos ")
#     m = (y[1] - y[0]) / (x[1] - x[0])
#     return m
# print(f'La pendiente de la ecuación es de: ', calculate_spole())


# Ecuación Cuadratica:  ax² + bx + c = 0.

# import cmath  # permite manejar soluciones complejas
#
# a = float(input("Ingrese a: "))
# b = float(input("Ingrese b: "))
# c = float(input("Ingrese c: "))
#
# def solve_quadratic_eqn(a, b, c):
#     # Cálculo del discriminante
#     discriminante = b**2 - 4*a*c
#
#     # Cálculo de las dos soluciones (pueden ser reales o complejas)
#     x1 = (-b + cmath.sqrt(discriminante)) / (2*a)
#     x2 = (-b - cmath.sqrt(discriminante)) / (2*a)
#
#     return x1, x2
#
# sol1, sol2 = solve_quadratic_eqn(a, b, c)
#
# print(solve_quadratic_eqn(a, b, c))
# print("Solución 1:", sol1)
# print('Solucion 2:', sol2)


# list = ['Edilson', 'Fabian', {'age': 21},{'Skill' : ['Java', 'Python', 'Spring Boot'] }]
# print(type(list))
#
# def print_list():
#
#     for i in list:
#         print(i)
#     return
#
# print_list()
#
# print(f'Mucho gusto mi nombre es {list[0]} {list[1]}, '
#       f'tengo{list[2]['age']} años y mis habilidades en programación son: '
#       f'{',' .join(list[3]['Skill'])}.')

# def reverse_list(array):
#     nueva_lista = []
#     # Recorremos desde el último índice hasta el primero
#     for i in range(len(array) - 1, -1, -1):
#         nueva_lista.append(array[i])
#     return nueva_lista
#
# mi_lista = [1, 2, 3, 4, 5]
# resultado = reverse_list(mi_lista)
# print(reverse_list(["A", "B", "C"]))
# print(resultado) # [5, 4, 3, 2, 1]
#
#

# list_letter = ['Edilson', 'Fabian', 'gomez', 'Torrado']
#
# def capitalize_list_item():
#
#     list_letter_capitalize = []
#     for letter in list_letter:
#         cap = letter.capitalize() # Si quiero que solo me ponga en Mayuscula la primera letra
#         #cap = letter.upper() Si quiero que me coloque en mayuscula toda la palabra en general
#         list_letter_capitalize.append(cap)
#     return list_letter_capitalize
#
# print(capitalize_list_item())

# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
# numbers = [2, 3, 7, 9]
# def add_item(lista, elemento):
#     lista.append(elemento)
#     return lista
#
# print(add_item(food_stuff , 'Banana'))
# print(add_item(numbers, 5))
#
# def remove_item(lista, elemento):
#     lista.remove(elemento)
#     return lista
#
# print(remove_item(food_stuff, 'Mango'))
# print(remove_item(food_stuff, 'Tomato'))
# print(remove_item(food_stuff, 'Milk'))
# print(remove_item(numbers, 5))


# def sum_of_numbers(numbers):
#     total = 0
#     for num in range(1, numbers + 1,2): # Si le pongo que me muestre de 2 en 2 eso numeros me los va a ordenar por items y me sumara solo los numeros que vayyan dde dos en dos
#         # hasta llegar al start que es num+1 es decir 6 entonces serian: [0,1,2,3,4,5,6] y ahi si me va a sumar de dos en 2 contando el indice del 0 no numeros y seria 1 + 3 + 5= 9
#         total += num
#     return total
# print(sum_of_numbers(5))
# print(sum_of_numbers(10)) # 0,1,2,3,4,5,6,7,8,9,10
# print(sum_of_numbers(100))


# def even_and_odds(numbers):
#     total_par = 0
#     total_imp = 0
#     for num in range(numbers + 1):
#         if num % 2 == 0:
#             total_par += 1
#            # total_par += num # La diferencia aca esta en qeu se va iterando numero por numero y aca cada ves que entre con el numero actual en esta condicion se le va a sumar al anterior
#         # siempre te va a realizar la suma del numero actual con el anterior mas no va a contar nuemros pares y lo mismo con la condicion de los impares.
#         elif num % 2 == 1:
#             total_imp += 1
#     print('The number of odds are ', total_par)
#     print('The number of evens are ', total_imp)
#     return total_par, total_imp
#
#
# even_and_odds(100)

#El factorial de un número es el resultado de multiplicar ese número por todos los números enteros positivos que son menores que él, hasta llegar al 1.
# def factorial(num):
#
#     factorial = num
#     for n in range(num - 1, -1, -1):
#         print(n)
#         factorial = factorial * n
#         if n == 1:
#             break
#     return factorial
#
# print(factorial(5))
#
# import math
# print(math.factorial(5))


# def is_empty(parametro):
#     # En Python, 'if not x' verifica si x está vacío, es cero o es None
#     if not parametro and parametro != 0:
#         return "El parámetro está vacío"
#     else:
#         return "El parámetro NO está vacío"
#
# # Pruebas
# print(is_empty(""))          # Vacío (String)
# print(is_empty([]))          # Vacío (Lista)
# print(is_empty(None))        # Vacío (None)
# print(is_empty("Hola"))      # NO está vacío


nums_estadistica = [1,56, 75, 34, 67, 300, 632, 2, 23, 56, 56, 98]

# def funtions_media(nums_estadistica):
#     total = 0
#     for i in nums_estadistica:
#         print(i)
#         #total += i
#         total = sum(nums_estadistica)
#         media = total / len(nums_estadistica)
#         print(len(nums_estadistica))
#     return media
#
# print('La media de la lista es de: ', funtions_media(nums_estadistica))

# def funtions_mediana(nums_estadistica):
#
#     nums_estadistica = sorted(nums_estadistica)
#     print(nums_estadistica)
#
#     n = len(nums_estadistica)
#
#     medio = n // 2
#
#     if n % 2 != 0:
#         return nums_estadistica[medio]
#     else:
#         valor1 = nums_estadistica[medio-1]
#         valor2 = nums_estadistica[medio]
#         return (valor1 + valor2) / 2
#
# print(funtions_mediana(nums_estadistica))
#
#
# import statistics
#
# datos = [1, 5, 3, 9, 7]
# print(statistics.median(datos))

#
#
# def funtions_moda(nums_estadistica):
#
#     frecuencia = {}
#
#     for num in nums_estadistica:
#         if not(num in frecuencia):
#             frecuencia.update({num:1})
#         elif num in frecuencia:
#             frecuencia[num] += 1
#
#     moda = None
#     maximum = max(frecuencia.values())
#     print(maximum)
#
#     for num, freq in frecuencia.items():
#         if freq == maximum:
#             maximum = freq
#             moda = num
#             print('Esta es la moda',moda)
#
#     return moda
#
# print(funtions_moda(nums_estadistica))
#
#

# nums_estadistica = [20,56, 75, 20,20, 20, 34, 67, 300, 300, 56, 632, 21, 23, 56, 56, 98]

# def funtions_rango(nums_estadistica):
#
#     maximo = nums_estadistica[0]
#     minimo = nums_estadistica[0]
#
#     for num in nums_estadistica:
#         if num > maximo:
#             maximo = num  # actualizamos el máximo
#         if num < minimo:
#             minimo = num  # actualizamos el mínimo
#
#
#     print('Maximo: ',maximo, 'Minimo: ', minimo)
#     print('El rango es:' , maximo-minimo)
#
# funtions_rango(nums_estadistica)
#
# nums_estadistica = [20,56, 75, 20,20, 20, 34, 67, 300, 300, 56, 632, 21, 23, 56, 56, 98]
#
# def funtions_media(nums_estadistica):
#     total = 0
#     for i in nums_estadistica:
#         #print(i)
#         #total += i
#         total = sum(nums_estadistica)
#         media = total / len(nums_estadistica)
#         # print(len(nums_estadistica))
#         media = int(media)
#     return media
#
# print('La media de la lista es de: ', funtions_media(nums_estadistica))
#
# import math
#
# def funtions_varianza(nums_estadistica):
#
#     media = funtions_media(nums_estadistica)
#     total = 0
#
#     for i in nums_estadistica:
#         desviacion_inicial = i - media
#         desviacion_cuadrada = desviacion_inicial ** 2
#         total += desviacion_cuadrada
#
#     varianza = total / len(nums_estadistica)
#     print("VARIANZA POBLACIONAL =", varianza)
#     return varianza
#
# funtions_varianza(nums_estadistica)
#
# nums_estadistica = [20,56, 75, 20,20, 20, 34, 67, 300, 300, 56, 632, 21, 23, 56, 56, 98]
#
# def funtions_media(nums_estadistica):
#     total = sum(nums_estadistica)
#     media = total / len(nums_estadistica)
#     return media
#
# def funtions_varianza(nums_estadistica):
#     media = funtions_media(nums_estadistica)
#     total = 0
#
#     for i in nums_estadistica:
#         desviacion_inicial = i - media
#         desviacion_cuadrada = desviacion_inicial ** 2
#         total += desviacion_cuadrada
#
#     varianza = total / len(nums_estadistica)  # POBLACIONAL
#     return varianza
#
# def funtions_desviacion_estandar(nums_estadistica):
#     varianza = funtions_varianza(nums_estadistica)
#     desviacion_estandar = varianza ** 0.5  # RAÍZ CUADRADA
#     return desviacion_estandar
#
# print("MEDIA =", funtions_media(nums_estadistica))
# print("VARIANZA =", funtions_varianza(nums_estadistica))
# print("DESVIACIÓN ESTÁNDAR =", funtions_desviacion_estandar(nums_estadistica))
#

# def funtions_greet(name = None):
#
#     if name is None or name == '':
#         print("Hello Invitado")
#     else:
#         print("Hello " + name)
#
# funtions_greet('Edilson')
# funtions_greet('')
# funtions_greet()

# def show_args(**kwargs):
#     result = ''.join([f'{clave}:{valor}' for clave, valor in kwargs.items()])
#     print('Resived: ', result)
#
#
# show_args(name="Alice ", age= 30,city = " New York")
#     # Received: name: Alice, age: 30, city: New York
# show_args(name="Bob ", pet="Fluffy, the bunny")
#     # Received: name: Bob, pet: Fluffy, the bunny

#
# num = int(input('Ingrese un numero:'))
#
# def is_prime(num):
#     if num <= 1:
#         return 'NO PRIMO'
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return 'NO PRIMO'
#
#     return 'PRIMO'
#
# print(is_prime(num))

#
# nums_list = [10, 20 , 20, 10, 20, 30, 30, 40, 50, 60, 40, 70]
#
# def show_repeated(nums_list):
#     seen = set()
#     repeated = set()
#
#     for num in nums_list:
#         if num in seen:
#             repeated.add(num)
#         else:
#             seen.add(num)
#
#     return repeated
#
# print(show_repeated(nums_list))
#
# list_types = ['Edilson', 'Gomez', 21, {'Skill': ['Python', 'Java', 'Scrum' ]} ]
# list_nums = [1, 2,3,4,5]
#
#
# def element_type(list_nums):
#     tipos = set(type(x) for x in list_nums)
#
#     if len(tipos) == 1:
#         return f'Todos los elemenetos son del tipo {tipos.pop().__name__}'
#     else:
#         return 'Hay varios tipos en la lista: ' + ', '.join(t.__name__ for t in tipos)
#
# print(element_type(list_nums))
#
# variable = input('Ingresa una variable: ')
#
# def variable_python(variable):
#
#     if variable.isidentifier() :
#         print('La variable',variable, 'es una buena practica de nombre')
#     else:
#         print('El nombre de la variable es inaducuada')
#
# variable_python(variable)


from countries_data import countries_json

languages = []
languages_repetidos = []

for country in countries_json:
    languages.append(country["languages"])
    if lenguaje == lenguaje:
        languages_repetidos.append(country["languages"])
        print('Languages repetidos', languages_repetidos)
print(languages)

def idiomas_world(language):
    count= 0
    while count < 10:
        sorted(languages)
        count = count + 1
        print('Estos son los paises ', countries_json)

idiomas_world(languages)



from countries_data import countries_json
from collections import Counter


def idiomas_mas_hablados(top_n=10):

    all_languages = []

    # Extraer todos los lenguajes del JSON
    for country in countries_json:
        all_languages.extend(country["languages"])

    # Contar repeticiones
    counts = Counter(all_languages)

    # Ordenar de mayor a menor
    sorted_languages = counts.most_common(top_n)

    return sorted_languages


# Mostrar los 10 idiomas más hablados
print(idiomas_mas_hablados(10))

def paises_mas_poblados(top_n=10):

    all_poblacion = []

    for country in countries_json:
        all_poblacion.append(country["population"])

    counts = Counter(all_poblacion)

    sorted_poblacion = counts.most_common(top_n)

    return sorted_poblacion

print(paises_mas_poblados(10))






