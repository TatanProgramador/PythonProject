
''''

OPERADORES LOGICOS

and

- Devuelve true solo si ambas condiciones son verdaderas
- Si alguna de condiciones es False, el resultado es False
- Con el and la prioridad la lleva el False en el caso en el que exista uno en dicho caso
'''

a = True
b = False

print(a and b) # False, por que b es falso y solo basta conb que una sola sea falsa
print(5 > 2 and 3 < 10), # True ambas son verdaderas


'''

  or

- Devuelve Fale solo si ambas condiciones son falsas
- Si alguna de las condiciones es True el resultado es True
- Con el Or la prioridad se la lleva el True en el caso de que exista uno en dicho caso 
'''

a = True
b = False
print (a or b)
print (4 > 2 or 3 < 10)


'''
  not 
  
- invierte el valor booleano 

'''

a = True
b = False

print(not a)
print (not b)


my_string = "Hello         78674865 khjkhkh khfghhihoihof ';';'  "
my_other_string = my_string

print(len(my_other_string))
print(my_other_string) , my_other_string
#print(len(my_string))

#Formateo

name, surname, age = 'Edilson' ,  'Gomez'  ,  20

print("Este es mi nombre {} {} y mi edad es {}"  .format(name, surname, age))
print("Este es mi nombre {0} {1} y mi edad es {2}"  .format(name, surname, age))
print("Este es mi nombre %s %s y mi edad es %d" %(name, surname, age))
print(f"Este es mi nombre {name} {surname} y mi edad es {age}")

''''
%s es para los datos Styring 
%d para los datos numericos enteros 
%f para los datos decimales 


Usando f-String 
- Se antepone una f antes de las comillas .
- Permite insertar variables y expresiones directamente en {}
- Mas rapido, mas flexible y puedes poner código dentro y es el mas actual 
'''

# Desenpaquetado

lenguaje = 'python'
a , b, c, d , e , f = lenguaje
print(a)
print(b)

# División

languaje_slice = lenguaje [0:6]
#print(languaje_slice)

# Funciones

print(lenguaje.capitalize())
print(lenguaje.upper())
print(lenguaje.lower())
print(lenguaje.count('p'))
print(lenguaje.capitalize())
print(lenguaje.isnumeric())
