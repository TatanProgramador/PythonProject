
#from day_module_12 import generate_full_name, sum_two_numbers, funtions_person, calculate_gravity
from day_module_12 import generate_full_name as full_name, sum_two_numbers as total, funtions_person as person, calculate_gravity as gravity
print(full_name('Edilson', 'Gomez'))
print(total(10, 20))
person = person()
print(person["country"])
mass = 100
gravity()
weight = mass * gravity()
print(weight)

import os
# Creando directorio
#os.mkdir("directory_namess")
# Cambiar el directorio actual
os.chdir(r"C:\Users\tatan\PycharmProjects\PythonProject")
# Obteniendo el directorio de trabajo actual
os.getcwd()
print("Directorio actual:", os.getcwd())

# Removienso directorio
os.rmdir('directory_names')
