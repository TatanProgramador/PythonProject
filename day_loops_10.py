# #
# #
# # # count = 0
# # # while count < 5:
# # #     print(count)
# # #     count += 1
# # #     # count = count + 1
# # # else:
# # #     print(count)
# #
# # # Estoy realizando lo mismo al usar count += 1 ya que aca me esta diciendo que va aumentar de uno en uno, y con la otra condicion count = count + 1  me esta diciendo que
# # # se va a mostrar el nuemro hasta que count sea igual a la condicion de while, esta tomando el ultimo conunt qwue es 4 y le suma unopara que quede en 5 entonces ya ahi la
# # # condicion de que count < 5 y el valor de count es 5 y 5 no es mayor que 5 y por ende mo se imprime.
# #
# # # count = 0
# # # while count < 5:
# # #     print(count)
# # #     count =count + 1
# # #     if count == 3:
# # #         break
# #
# # count = 0
# # while count < 5:
# #     if count == 3:
# #         count += 1
# #         continue
# #     print(count)
# #     count = count + 1
# #
# #         # 0, 1, 2, 4
# #
# # numbers = [0, 1, 2, 3, 4, 5]
# #
# # for number in numbers:
# #     print(number)
# #
# # lenguaje = 'Python'
# #
# # for letra in lenguaje:
# #     print(letra)
# #     if letra == 't':
# #         break
# #
# # for i in range(len(lenguaje)): # 6
# #     print(lenguaje[i])
# #
# # # Este for no recorre las letras directamente sino que, len(lenguaje) devuelve la longitd del string que es 6 y range genera una secuencia de numeros
# # # y en lenguaje[i] i toma cada uno de esos valores y accede a la letra que esta en esa posicion
# #
# # numbers = (0, 1, 2, 3, 4, 5)
# # for number in numbers:
# #     print(number)
# #
# # person = {'First Name': 'John',
# #           'Last Name': 'Smith',
# #           'Age': 19,
# #           'Country': 'Finland',
# #           'is_married': False,
# #           'skill' : ['Java', 'Python', 'Scrum', 'Spring Boot'],
# #           'adrress': {
# #               'stret': 'Space stret',
# #               'zipcode' : '02010'
# #           }
# #
# #           }
# #
# # for key in person:
# #     print(key)
# #
# # for key, values in person.items():
# #     print(key, values)
# #
# # it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# # for company in it_companies:
# #     print(company)
# #
# # ##
# #
# # # numbers = (0,1,2,3,4,5)
# # # for number in numbers:
# # #     print(number)
# # #     if number == 3:
# # #         break
# #
# #
# # numbers = (0,1,2,3,4,5)
# # for number in numbers:
# #     print(number)
# #     if number == 3:
# #         continue
# #     print('El siguiente número debería ser ', number + 1) \
# #         if number != 5 else print("final del bucle") # for short hand conditions need both if and else statements
# # print('outside the loop')
# #
# # lst = list(range(11))
# # print(lst)
# # st = set(range(1, 11))
# # print(st)
# #
# # lst = list(range(0, 13, 2))
# # print(lst)
# #
# # st = set(range(0, 13, 2))
# # print(st)
# #
# # for number in range(11):
# #     print(number)   # prints 0 to 10, not including 11
# #
# # for key in person:
# #     if key == 'skill':
# #         for skill in person['skill']:
# #             print(skill)
# #     else:
# #         print('Ejecucion terminada')
# #
# # for number in range(6):
# #     pass
# #
# # numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #
# # for number in numbers:
# #     print('For List', number)
# #
# # for number in range(11):
# #     print('For Range',number)
# #
# # count = 0
# # while count <= 10:
# #     print('While',count)
# #     count += 1
# #     #count = count + 1
# #
# # for number in range(10, -1, -1):
# #     print('For invertido',number)
# #
# #
# # count = 10
# # while count >= 0:
# #     print('While invertido',count)
# #     count = count - 1
# #
# # count = 0
# # while count < 7:
# #     print('#' * count)
# #     count += 1
# #
# #
#
#
# # count = 0
# # while count == 0:
# #     print('# # # # # # # #')
# #     count += 1
# #     while count <= 7:
# #         print('# # # # # # # #')
# #         count += 1
#
# fila = 0
# while fila < 8:
#     columna = 0
#     while columna < 8:
#         print('#', end=' ')
#         columna += 1
#     print()
#     fila += 1
#
# for i in range(11): # 6
#     # print(i , i)
#     print(i, "*", i, "=", i * i)
#
# count = 0
# while count <= 10:
#     print(count, "*", count, '=', count * count)
#     count += 1
#
# lst = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
# for item in lst:
#     print(item)
#
# for i in range(100):
#     if i % 2 == 0:
#         print(i) # Numeros pares
#
# for i in range(100):
#     if i % 2 == 1:
#         print(i)
#
# for i in range(100):
#     print(i)



# suma = 0
# for i in range(101):
#     print(i)
#     suma = suma + i
# print(f'La suma de todos los numeros es de: ',{suma})
#
#
# suma_pares = 0
# suma_impares = 0
# for i in range(101):
#     if i % 2 == 0:
#         suma_pares = suma_pares + i
#         print(i)
#     elif i % 2 == 1:
#         suma_impares = suma_impares + i
# print(f'La suma de todos los numeros pares es de: ', {suma_pares}, 'y la suma de todos los impares es de: ', {suma_impares})
#Ve a la carpeta de datos y usa el archivo Countries.py . Recorre los países y extrae todos los que contengan la palabra " land" .

# from countries import countries
#
# for countri in countries:
#     if 'land' in countri :
#         print (countri)
#
# frutas = ['banana', 'naranja', 'mango', 'limón']
#
# frutas_invertidas = []
#
# for i in range(len(frutas)-1, -1, -1):
#     frutas_invertidas.append(frutas[i])
# print(frutas_invertidas)
#
#
# name_comple = {'Primer Nombre' : 'Edilson', 'Segundo Nombre' : 'Fabian', 'Primer Apellido' : 'Gomez', 'Segundo Apellido' : 'Torrado'}
#
# name_inevertido = {}
#
# for key in reversed(name_comple):
#     name_inevertido[key] = name_comple[key]
# print(name_inevertido.keys())
# print(name_inevertido.values())

from countries_data import countries_json
#
# total_general = 0
#
# for country in countries_json:
#     print(country['name'], country['languages'])
#     suma_lenguaje = len(country['languages'])
#     total_general = total_general + suma_lenguaje
#
# print(total_general)

# conteo_idiomas = {}
#
# for country in countries_json:
#     for language in country['languages']:
#         if language in conteo_idiomas:
#             conteo_idiomas[language] += 1
#         else:
#             conteo_idiomas[language] = 1
#
# idiomas_ordenados = sorted(
#     conteo_idiomas.items(),
#     key=lambda item: item[1],
#     reverse=True
# )
#
# top_10_idiomas = idiomas_ordenados[:10]
#
# for idioma, cantidad in top_10_idiomas:
#     print(idioma, cantidad)


paises_ordenados = sorted(
    countries_json,
    key=lambda country: country['population'],
    reverse=True
)

top_10_poblados = paises_ordenados[:10]

for country in top_10_poblados:
    print(country['name'], country['population'])


