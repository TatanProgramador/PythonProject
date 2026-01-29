# #
# # ##Operadores aritmeticos
# #
# # print('addition: ', 3 + 3)
# # print('subtraction', 3 - 5)
# # print('multiplication', 3 * 5)
# # print('division', 4/2 )
# # print('dividion', 6 / 2)
# # print('division', 7 / 2)
# # print('division without the remainder', 7 // 2)
# # print('division without the remainder', 7 // 3)
# # print('modules', 100 % 4 )
# # print('exponentiation ', 3 ** 2)
# #
# # # Complex numbers
# # print('Complex number: ', 1 + 1j)
# # print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))
# #
# # # Calculating area of a circle
# #
# # radius = 10
# # area_of_circle = 3.14 * radius**2
# # print('Radius: ', radius)
# # print('Area of circle: ', area_of_circle)
# #
# # # Calculating area of rectangle
# #
# # legth = 10
# # width = 20
# # area_of_rectangle = legth * width
# # print('Area of rectangle: ', area_of_rectangle )
# #
# # # Calculating a weight of a object
# #
# # mass = 75
# # gravity = 9.81
# # weight = mass * gravity
# # print('mass:', mass)
# # print('weight:', weight)
# #
# # # Operadores de comparacion
# #
# # print(3 > 2)
# # print(3 >= 2)
# # print(3 < 2)
# # print(2 < 3)
# # print(2 <= 3)
# # print(3 == 2)
# # print(3 != 3)
# # print(len('mango') == len('3rcos'))
# # print(len('colombia') != len('colombiaa'))
# # print('True == True: ', True == True)
# # print('False == False: ', False == False)
# #
# # print(1 is not 2)
# # print('?,' in 'Amigo3?,')
# # print(4 is 2**2)
# #
# # print('1 is 1', 1 is 1)                   # True
# # print('1 is not 2', 1 is not 2)           # True
# # print('A in Asabeneh', 'A' in 'Asabeneh') # True
# # print('B in Asabeneh', 'B' in 'Asabeneh') # False
# # print('coding' in 'coding for all') # True
# # print('a is an:', 'a' is 'an')      # Fale
# # print('4 is 2 ** 2:', 4 is 2 ** 2)   # True
# #
# # ###Operadores Logicos and, or, on
# # ### And me devuelve True si los dos son True
# # ### Or me duvuelve True si almenos uno de ellos es verdadero
# # ### not me invierte el resultado de un valor de True a False y viseverda
# #
# # print(4 == 4 and 3 < 4) ##(Conjuncion ) Todos los elementos deben ser True
# # print(3 == 4 or 3 == 2) ##(Disyunción ) Almenos uno de los dos debe ser True
# # print('Este es el ultimo ', not 3 < 4) ## Me retorna el valor contrario al esperado
# #
# #
# # print(3 > 2 and 4 > 3) # True
# # print(3 > 2 and 4 < 3) # False
# # print(3 < 2 and 4 < 3) # False
# # print('True and True: ', True and True) # True
# # print(3 > 2 or 4 > 3)  # True
# # print(3 > 2 or 4 < 3)  # True
# # print(3 < 2 or 4 < 3)  # False
# # print('True or False:', True or False) # True
# # print(not 3 > 2)   # False
# # print(not True)      # False
# # print(not False)     # True
# # print(not not True)  # True
# # print(not not not not False) # True  Cada ves que se ponga un not se va a invertir el valor
# #
# # ## Exercise
# #
# # edad = 20
# # altura = 1.80
# # num_complex = 16 + 3j
# #
# # #base = input('Ingresa la base del triangulo')
# # #print(f"Este es el valor de la base {base}")
# #
# # #altura = input('Ingresa la altura del triangulo')
# # #print(f"Este es el valor de la altura {altura}")
# #
# # #int_base = int(base)
# # #int_altura = int(altura)
# #
# # #print(type(int_base))
# # #print(type(int_altura))
# # #area = (int_base * int_altura / 2)
# # #print(f"Este es el valor de la area {area}")
# #
# # #largo = int(input('Ingresa la largo del rectangulo'))
# # #ancho = int(input('Ingresa la ancho del rectangulo'))
# #
# # #area = largo * ancho
# #
# # #print(f"Este es el valor de la area del rectangulo{area}")
# #
# # #perimetro = 2 * (largo + ancho)
# #
# # #print(f"El perimetro del rectangulo es {perimetro}")
# #
# #
# # #
# # # radius = int(input('Ingresa el radio del circulo'))
# # # pi = 3.14
# # # area = pi * radius ** 2
# # # print(f'El area del circulo es {area}')
# # #
# # # circunference = 2 * pi * radius
# # #
# # # print('La circunferencia del circulo es ', circunference)
# #
#
#

#
# # print(f'Este es el tamaño de var 1: {len(var_1)}')
# # print(f'Este es el tamaño de var 2: {len(var_2)}')
#
# # if len(var_1) < len(var_2):
# #     print('Esto no cva a salir por que el ejercicio me esta pidiendo que realize una comparacion falsa')
#
# # print(len(var_1) == len(var_2))
#
# # if 'on' in var_1 and 'h' in var_2:
# #     print('si se encuentran dichas palabras')
# # else:
# #     print('no se encuentran dichas letras')
#
# frase = 'Espero que este curso no este lleno de jerga'
#
# # if 'jerga' in frase:
# #     print(frase)
#
# # print( 'jerga' in frase, 'Si esta presente esa palabra en la frase')
#
# contiene_jerga = 'jerga' in frase
#
# print(f'La frase si contiene la palabra jerga:{contiene_jerga}')
#

# if not 'on' in var_1 and var_2:
#     print('No hay esas letras en la palbras')
# else:
#     print('Si estan esas letras en la palabras')
#
# var_1 = 'python'
# var_2 = 'dragon'
#
# print(f'Esta es la longitud de var 1: {len(var_1)}')
#
# len_var1 = len(var_1)
#
# print(type(var_1))
#
# flotante = float(len_var1)
# var_1 = flotante
# print(type(var_1))
# print(var_1)
#
# cadena = str(len_var1)
# var_1 = cadena
#
# print(type(var_1))
# print(var_1)

# num_ingresado = int(input("Ingresar un numero para verificar si el numero es par o impar: "))
# #print(f'El numero ingresado es este: {num_ingresado} ')
#
# if num_ingresado % 2 == 0:
#     print ('El numero es par')
# else:
#     print ('El numero es impar')

# num_1 = 7 // 3
#
# convertido = 2.7
#
# num_int = int(convertido)
# print(num_int)
#
# if num_int == num_1:
#     print('Los valores son iguales')

# if type('10') == type(10):
#     print('el Type de los dos datos son iguales')
#
# Str1 = '9.8'
#
# num = int(Str1)
# print(num)
#
# if int('9.8') == 10:
#     print('Los datos son iguales')
# else:
#     print('Los datos son diferentes')
#
# horas_trabajadas = int(input('Ingrese las horas trabajadas'))
# presio_hora = int(input('Ingrese la presio hora'))
#
# total_salario = horas_trabajadas * presio_hora
#
# print(f'Total a pagar: {total_salario}')

# edad = int(input("Edad: "))
#
# edad_segundos = (edad * 31.536)
#
# print('La cantidad de sugundos que podrias vivir son: ' , edad_segundos)

# print('1 1 1 1 1')
# print('2 1 1 4 8')
# print('3 1 3 9 27')
# print('4 1 4 16 64')
# print('5 1 5 25 125')

for n in range(1, 6):
    print(n, 1, n, n**2, n**3)
