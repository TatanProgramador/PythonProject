#
# miltiline_string = '''Este es un texto multilinea'''
#
# print(miltiline_string)
#
# first_name= 'Edilson'
# last_name= 'Gomez'
# space = ' '
# full_name = first_name + ' ' + last_name
#
# print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
# print('Days\tTopics\tExercises') # adding tab space or 4 spaces
# print('Day 1\t5\t5')
# print('Day 2\t6\t20')
# print('Day 3\t5\t23')
# print('Day 4\t1\t35')
# print('This is a backslash  symbol (\\)') # To write a backslash
# print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote
#
#
# print(full_name)
#
# print('Este es un ejemplo \nde doble linea')
# print('Este es un ejemplo \t5 de tabular')
# print('This is a backslash  symbol (\\)') # To write a backslash
# print('In every programming language it starts with \"Hello, World!\"')
#
#
# # Strings only
# first_name= 'Edilson'
# last_name= 'Gomez'
# lenguaje = 'Python'
# tiempo = 10.4
#
# formated_string = 'Yo soy %s %s, y estoy estudiando %s, en los cuales llevo %d meses practicandolo' %(first_name, last_name, lenguaje, tiempo)
#
# print(formated_string)
#
# # Strings  and numbers
# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formated_string_area = 'Él area de dicho radio:%d es de %d ' %(radius, area)
# print (formated_string_area)
#
# formated_string_llaves_area = 'El area de dicho radio: {} es de {}'.format(radius, area)
# print(formated_string_llaves_area)
#
# python_libraries = ['Django ,Flask, Numpy, Panda']
# formated_string_libraries= 'Las librerias de Python mas utilizadas son: %s'% (python_libraries)
# print(formated_string_libraries)
#
# first_name= 'Edilson'
# last_name= 'Gomez'
# lenguaje = 'Python'
# area_desarrollo = 'Backend'
#
# formated_string_llaves = 'Mi nombre es {} {}, y estoy estududiando el lenguiaje de {} para desempeñarme en el area de {}'.format(first_name, last_name, lenguaje, area_desarrollo)
# print(formated_string_llaves)
#
#
# a = 10
# b = 20
#
# print('abstraccion {} + {} = {}'.format(a, b , a + b))
# print('substraccion {} - {} = {}'.format(a, b, a - b))
# print('multiplicacion {} * {} = {}'.format(a, b, a * b))
# print('division {} / {} = {}'.format(a, b, a / b))
# print('exponencial {} ** {} = {}'.format(a, b, a ** b))
# print('modulo {} % {} = {}'.format(a, b, a % b))
# print('{} // {} = {}'.format(a, b, a // b))
#
#
# print(f'{a} + {b} =' , a + b)
# print(f'{a} - {b} =' , a - b)
#
# lenguaje = 'Python'
#
# a,b,c,d,e, f = lenguaje
# print(a, b, c, d, e,f)
#
# first_later = lenguaje[0]
# print(first_later)
# second_later = lenguaje[1]
# print(second_later)
#
# text = "hoy es un hermoso dia en el pueblo"
# print(text.capitalize())
# print(text.count('e'))
# print(text.endswith('lo'))
#
# text = 'hoy es \tun hermoso dia \ten el pueblo'
# print(text.expandtabs(20))
# print(text.find('f'))
# print(text.rfind('e'))
#
# challengue = 'Estamas estudiando Python'
# sub_string = 'a'
# print(challengue.index(sub_string, 5))
#
# challenge = '21123'
# sub_string = 'da'
# #print(challenge.index(sub_string))  # 7
# #print(challenge.index(sub_string, 6)) # error
# print(challenge.isalnum()) # Deviulve tru si solo en dicha cadenas hay datos alfanumericos nada de espacion ni caraceres especiales
# print(challenge.isalpha()) # Falso por que contiene numeros y eso me valida de que solo contenga caracteres alfabeticos
# print(challenge.isdecimal()) #False por que contiene tanto caracteres alfabeticos como decimales
# challenge = 'Trirty'
# print(challenge.isdigit())
# challenge = '0123456789'
# print(challenge.isdigit())
# challenge = '\u00B2'
# print(challenge.isdigit())
# num = '19993'
# print(num.isnumeric())
# num = 'Añあ😀'
# print(num.isnumeric())
#
# "ñ".encode('utf-8')
#
# texto = "ñ 😀"
#
# print(texto)              # Muestra los caracteres
# print(len(texto))         # 3 caracteres
# #print(texto.encode())     # b'\xc3\xb1 \xf0\x9f\x98\x80'
# print(texto.encode())
#
# cadena = "Hola ñ 😀"
# print(cadena.encode("utf-8"))
#
#
# for b in cadena.encode("utf-8"):
#     print(hex(b))
#
# c = "😀"
# print(ord(c))
#
# "😀".encode("utf-8")
#
# # Unicode es el estandar universal que define todos los caracteres de todos los idiomas emojis, signos, simbolos y a cada uno le asigna un numero único llamado punto de codigo
# # y ahi es donde estra el utf-8 para guardar ese punto de codigo en bytes para que sea interpretado.
#
# challenge = '30DaysOfPython'
# print(challenge.isidentifier())
# challenge = 'days_of_python'
# print(challenge.isidentifier()) # Verifica si una cadena es un nombre valido para definir un avariable
#
# challengue_two = 'edilson'
# print(challengue_two.islower())# verifica que los caracteres esten definidos en minuscula
#
# challengue = 'EDILKOSN'
# print(challengue.isupper()) # Verifica que los caracteres esten definidos en mayusculas
#
# challengue = ['Html', 'Python', 'Java', 'Typescrip']
# result = '#' .join(challengue)
# print(result)
#
# challengue = 'Este es el ejemplo de strip'
# print(challengue.strip('Esip'))
#
# challengue = 'Este es el ejemplo de remplace'
# print(challengue.replace('Este', 'Python'))
# challengue = (challengue.replace('Este', 'Python'))
# print(challengue.replace('Python', 'Java'))
#
# challengue = 'Este es el ejemplo de split'
# print(challengue.split())
# challengue = (challengue.split()) # Lo que hace es cada palabra separada por espacion lo hace un elemento
# print(len(challengue))
#
# challenge = 'Este es el ejemplo de title que me va a poner mayusculas en todas las palabras al comienzo'
# print(challenge.title())
#
# challengue = 'Este es el ejemplo que me va a PONER las letras en viservera de mayuscula a miniscula y vISEVVERSA 74853843864683'
# print(challengue.swapcase())
#
# challengue = 'Comprueba si la cadena comienza con la cadena especificada'
# print(challengue.startswith('Compr'))
#
#

#Ejercies

cadena_concatenada = ['Thirthy', 'Days', 'of', 'Python']

print(type(cadena_concatenada))
cadena_join = ' ' .join(cadena_concatenada)
print(type(cadena_join))
print(cadena_join) # Con el metodo join que me lo da Python puedo pasar una lista a un string

cadena_concatenada = ['Conding', 'For', 'All']
print(type(cadena_concatenada))

cadena_join = ' ' .join(cadena_concatenada)
print(cadena_join)

compañia = 'Coding For All'
print(compañia)
print(len(compañia))
print(compañia.upper())
print(compañia.lower())
print(compañia.capitalize())
print(compañia.title())
print(compañia.swapcase())
print(compañia.split())
