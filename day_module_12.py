from zoneinfo import reset_tzpath

from day_diccionary_08 import primary_dict
from day_list_05 import cadena
from day_tuples_06 import union

#
# def generate_full_name (firstname, lastname):
#     return firstname + " " + lastname
#
# def sum_two_numbers (number1, number2):
#     return number1 + number2
#
# def funtions_person():
#     person = {
#         "first_name": "Fabian",
#         "last_name": "Torrado",
#         "country": "United States",
#         "population": 13452,
#         "flag": "https://restcountries.eu/data/aia.svg",
#         "email": "",
#         "website": "https://restcountries.eu/data/aia.svg",
#     }
#     return person
#
# def calculate_gravity():
#     gravity = 9.81
#     return gravity
#
# import sys
# #print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
# #print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
# print('Esta es la versión', sys.version)
# print('Este es el maximo', sys.maxsize)
# print('Este es el path', sys.path)
#
# from statistics import *
#
# ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
# print(mean(ages))
# print(median(ages))
# print(mode(ages))
# print(stdev(ages))
#
# import math
# print('PI',math.pi)           # 3.141592653589793, pi constant
# print('sqrt raiz cuadrada', math.sqrt(2))      # 1.4142135623730951, raiz cuadrada
# print('pow exponencial',math.pow(2, 3))    # 8.0, exponential function
# print('floor redondeadoal minimo', math.floor(9.81))  # 9, redondeado al minimo
# print('ceil redondeado al maximo',math.ceil(9.81))   # 10, redondeadfo al maximo
# print('log10 logaritmo con base 10',math.log10(100))   # 2, logarithm with 10 as base
#
# from math import pi
#
# print('pi en radians',pi)
#
# # Cambair ewl nombre de la funcion
# from math import pi as pipi
# print('pipi en radians',pipi)
#
# import string
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
#
# from random import randint, random
#
# print(random())
# print(randint(1,10))

import random
import string

# caracteres = int(input('Ingresa el numero de caracteres del usuario: '))
# ids = int(input('Ingrese el nuemro de ids a generar: '))
# ids_iterable = 0
#
# def random_users_id():
#     list_letras = []
#     letras = string.ascii_letters
#     list_random_letras = []
#     list_numeros = []
#     numeros = string.digits
#     list_random_numeros = []
#     union_list = []
#     caracter_letras = caracteres / 2
#     caracteres_numeros = caracteres / 2
#
#     for i in letras:
#         list_letras.append(i)
#         tamaño = len(list_letras)
#         if tamaño > caracter_letras:
#             break
#         random_letras = random.choice(letras)
#         i = random_letras
#         list_random_letras.append(i)
#
#     for i in numeros:
#         list_numeros.append(i)
#         tamaño = len(list_numeros)
#         if tamaño > caracteres_numeros:
#             break
#         random_numeros = random.choice(numeros)
#         i = random_numeros
#         list_random_numeros.append(i)
#
#     union_list = list_random_letras + list_random_numeros
#     random.shuffle(union_list)
#     cadena = ''.join(union_list)
#
#     return cadena
#
# for i in range(ids):
#     print(random_users_id())

import random

# def list_of_hexa_colors():
#
#     simbolos = [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
#     list_hexa = []
#     limite_simbolos = 6
#     i = random.shuffle(simbolos)
#
#     for i in simbolos:
#         if len(list_hexa) < limite_simbolos:
#             list_hexa.append(i)
#             random.shuffle(simbolos)
#         elif limite_simbolos == len(list_hexa):
#             list_hexa.insert(0, '#')
#
#     #print(list_hexa)
#     cadena = ''.join(str(x) for x in list_hexa)
#     print(cadena)
#
#     return
#
# list_of_hexa_colors()


def generate_colors(contenido, num ):

    simbolos_hexa = [0, 1, 2, 3, 4, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
    list_hexa = []
    list_resultados_hexa = []
    list_resultados_rgb = []
    limite_simbolos_hexa = 6
    random.shuffle(simbolos_hexa)
    iterador = 0

    while iterador < num:
        list_hexa = []
        random.shuffle(simbolos_hexa)
        if contenido == 'hexa':
            for i in simbolos_hexa:
                if len(list_hexa) < limite_simbolos_hexa:
                    list_hexa.append(i)
                elif len(list_hexa) == limite_simbolos_hexa:
                    list_hexa.insert(0, '#')

            cadena = ''.join(str(x) for x in list_hexa)
            list_resultados_hexa.append(cadena)
        elif contenido == 'rgb':
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                color = f"rgb({r}, {g}, {b})"
                list_resultados_rgb.append(color)

        iterador += 1

    if contenido == 'hexa':
        return list_resultados_hexa
    else:
        return list_resultados_rgb

print(generate_colors(contenido='rgb', num=6))
print(generate_colors(contenido='hexa', num=6))

import random

def shuffle_list(lista):
    random.shuffle(lista)
    return lista

print(shuffle_list(['Edilson', 'Gomez', 21, {'skills': ['java', 'Python']}, 'Masculino']))

def matriz_seven_numbers():

    nums = range(0,10)
    list_nums = []
    limite = 7

    for i in range(0, 10):
        if len(list_nums) < limite:
            list_nums.append(i)
        random.shuffle(list_nums)
    return list_nums

print(matriz_seven_numbers())


#Version mejorada por ia

# import random
# import string
#
# def random_users_id():
#     letras = string.ascii_letters
#     numeros = string.digits
#
#     list_random_letras = [random.choice(letras) for _ in range(3)]
#     list_random_numeros = [random.choice(numeros) for _ in range(3)]
#
#     union_list = list_random_letras + list_random_numeros
#     random.shuffle(union_list)
#
#     return ''.join(union_list)
#
# print(random_users_id())
# print(random_users_id())
# print(random_users_id())

# from random import randint
#
# def rgb_color_gen():
#
#     list_rgb = []
#
#     while len(list_rgb) < 3:
#         values = randint(0, 255)
#         list_rgb.append(values)
#
#     return list_rgb
#
# print(rgb_color_gen())


# vercion mejorada con ia
#
# import random
#
# def list_of_hexa_colors(n):
#     simbolos = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
#     colores = []
#
#     for _ in range(n):
#         list_hexa = []
#         for _ in range(6):
#             list_hexa.append(random.choice(simbolos))
#         color = "#" + ''.join(list_hexa)
#         colores.append(color)
#
#     return colores
#
# print(list_of_hexa_colors(5))

# def list_of_rgb_colors(n):
#
#     list_rgb = []
#     for i in range(n):
#         r = random.randint(0, 255)
#         g = random.randint(0, 255)
#         b = random.randint(0, 255)
#
#         color = f"rgb({r}, {g}, {b})"
#         list_rgb.append(color)
#
#     return list_rgb
#
# print(list_of_rgb_colors(4))



















