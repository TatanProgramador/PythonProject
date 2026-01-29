
# Cuenta el número de caracteres (incluyendo espacios)
print(len('Hello, World!'))

# Convierte número a string
valor_str = str(10)
print(valor_str)
print(type(valor_str))

# Convierte string a número
valor_int = int("10")
print(valor_int)
print(type(valor_int))

# Convierte entero a decimal (float)
valor_float = float(10)
print(valor_float)
print(type(valor_float))


num_int = int(10.5)
print(num_int)
# Toma un dato ingresado por el usuario
#name = input('Enter your name: ')
#print(name)

#help('keywords')

print(min(5, 10, 40, 53, 100))
print(max(5, 10, 30, 23, 45, 23))
print(min([5,  78, 4]))
print(max([5,  78, 4]))
print(sum([30, 83, 56]))

#Valiables en Python

first_name = 'Edilson'
last_name = 'Gomez'
country = 'Colombia'
city = 'Abrego'
age = 20
is_married = False
skills = ['Java', 'Python', 'Sql', 'JavaScript']
person_info = {
    'first_name : Edilson',
    'last_name : Gomez',
    'country : Colombia',
    'city : Abrego',
    'age : 20',
    'is_married : False'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

#first_name = (input("What is your name?"))
#last_name = (input("What is your last name?"))

name_global = first_name + ' ' + last_name
print(f"El nombre y apellido del usuario es {name_global}")

resultado = zip([3, 5, True], [6, 4, 1.3], ['Edilson', 'Gomez', 45], [10, 10, 56])
print(type(resultado))
print(list(resultado))

num_int = 100
print('Numero entero',num_int)
num_float = float(num_int)
print('Numero decimal', num_float)

num_FLOAT = 3.1416
print('Numero decimal', num_FLOAT)
num_int = int(num_FLOAT)
print('Numero entero', num_int)

num_int = 1416
print('Numero int', num_int)
num_string = str(num_int)
print('Numero string', num_string)
print(type(num_string))
print('Numero string:', repr(num_string))

num_string = '1092'
print('Numero string', num_string)
num_int = int(num_string)
print('Numero int', num_int)
print(type(num_int))
num_float = float(num_string)
print('Numero float', num_float)

string = 'Edilson'
print(string)
lista = list(string)
print(lista)