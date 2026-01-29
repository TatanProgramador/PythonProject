# num = int(input("Ingrese un número"))
# if num > 0:
#     print('Este numero es positivo')
# elif num < 0:
#     print('Este numero es negativo')
# elif num == 0:
#     print('Este numero es zero')
# else:
#     print('Este numero no es positivo')
#
#
# if num > 0:
#     if num % 2 == 0:
#         print('Este numero es par')
#     else:
#         print('Este numero es impar')
# elif num == 0:
#         print('Este numero es cero')
# else:
#     print('Este numero es negativo')

# Evitamos las condiones anidadas usando el operador logico and


# if num > 0 and num % 2 == 0:
#     print('Este numero es positivo y es par')
# elif num > 0 and num % 2 != 0:
#     print('Este numero es positivo y es impar')
# elif num == 0:
#     print('Este numero es zero')
# else:
#     print('Este numero es negativo')


# users = 'Tatan'
# acces_level = 3
# users_ingresado = input('Ingrese su usuario')
# level_ingresado = int(input('Ingrese su level'))
#
# if users == users_ingresado or level_ingresado  >= 4:
#     print('Acceso consedido ')
# else:
#     print('No Acceso consedido')

#exercise

# edad = int(input('Ingrese su edad'))
# años_faltantes = 18 - edad
#
# if edad >= 18:
#     print('Tiene edad suficiente para conducir')
# elif edad<18:
#     print('No eres apto para conducir te faltan: ', años_faltantes , 'años')

# my_age = 21
# print("LA QUE SE DEBE EVALUAR ES ESTA QUE SOY EL QUE MANDA", my_age)
# your_age = int(input("Tu edad es: "))
# singular = 'año'
# plural = 'años'
# diferencia = abs(my_age - your_age)
#
# if my_age > your_age:
#     if diferencia == 1:
#         print("Yo soy mayor que tu por", diferencia ,  singular)
#     else:
#         print('Yo soy mayor que tu por', diferencia , plural)
#
# elif my_age < your_age:
#     if diferencia == 1:
#         print('Tu eres mayor que yo por', diferencia , singular)
#     else:
#         print('Tu eres mayor que yo por', diferencia, plural)
#
# else:
#     print('Tenemos la misma edad')

# if my_age > your_age and diferencia == 1:
#     print("Yo soy mayor que tu por", diferencia ,  singular)
# elif my_age > your_age and diferencia > 1:
#     print('Yo soy mayor que tu por', diferencia, plural)
# elif my_age < your_age and diferencia == 1:
#     print('Tu eres mayor que yo por', diferencia , singular)
# elif my_age < your_age and diferencia > 1:
#     print('Tu eres mayor que yo por', diferencia, plural)
# else:
#     print('Tenemos la misma edad')
#
# a = int(input("Ingresa un numero: "))
# b = int(input("Ingresa otro numero: "))
#
# if a > b:
#     print('A es mayor que b')
# elif a < b:
#     print('A es menor que b')
# else:
#     print('A es igual a b')


# num = int(input('Cual es tu calificacion para darte una representacion en letras'))
#
# if num >= 90 and num <= 100:
#     print('Tu calificacion es A')
# elif num >= 80 and num <= 89:
#     print('Tu calificacion es B')
# elif num >= 70 and num <= 79:
#     print('Tu calificacion es C')
# elif num >= 60 and num <= 69:
#     print('Tu calificacion es D')
# elif num <= 50 and num >= 0:
#     print('Tu calificacion es F')
# else:
#     print('Tu calificacion no esta en el rango estipulado')

# mes = input('Ingrese el mes en el que se encuentra para verificar la temporada').strip().lower()
#
# list_otoño = ['septiembre','octubre','noviembre']
# list_invierno = ['diciembre', 'enero', 'febrero']
# list_verano = ['junio', 'julio', 'agosto']
#
# if mes in list_otoño:
#     print('Estas en la temporada de otoño')
# elif mes in list_invierno:
#     print('Estas en la temporada de invierno')
# elif mes in list_verano:
#     print('Estas en la temporada de verano')
# else :
#     print('No se encuentra en la temporada')

# Si una fruta no existe en la lista, añádela e imprime la lista modificada. Si la fruta existe, print('Esa fruta ya existe en la lista')
# fruits = ['banana', 'orange', 'mango', 'lemon']
#
# new_fruit = input('Ingresa una fruta y si no esta en la lista se agregara')
#
# if new_fruit in fruits:
#     print('El nombre del fruto es igual a la lista')
# elif new_fruit not in fruits:
#     agregar_fruit = fruits.insert(0, new_fruit)
#     print('La fruta se a agregado a la lista')
#
# print(fruits)

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# variable = 'Python'
#
# if 'skills' in person:
#     print(person.get('skills')[2])
#     if 'skills' in person:
#         if 'Python' in person['skills']:
#             print('La persona tiene la habilidad de Python')
#
#         else:
#             print('La persona no tiene la habilidad de Python')

#Si las habilidades de una persona solo tienen JavaScript y React, imprima ('Él es un desarrollador front-end'), si las habilidades de la persona tienen Node, Python,
# MongoDB, imprima ('Él es un desarrollador back-end'), si las habilidades de la persona tienen React, Node y MongoDB, imprima ('Él es un desarrollador fullstack'),
# de lo contrario imprima ('título desconocido') - ¡para obtener resultados más precisos, se pueden anidar más condiciones!

# if 'JavaScript' in person['skills'] and 'React' in person['skills']:
#     print('El es un desarrollador FrontEnd')
# elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
#     print('El es un desarrollador BackEnd')
# elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
#     print('El es un desarrollador FullStack')
#
# else:
#     print('Titulo desconocido')
#
# Si la persona está casada y vive en Finlandia, imprima la información en el siguiente formato:

if person['is_married'] and person['country'] == 'Finland':
    print('Asabeneh Yetayeh lives in Finland. He is married.')

else :
    print('No se cumple la condicion')
