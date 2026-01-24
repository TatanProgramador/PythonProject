# Tuples #

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (20, 1.80, "Edilson", "Gomez")
my_other_tuple = (20, 1.80, "Dilia", "Rosa")
print(my_tuple)
print (type(my_tuple))

print (my_tuple[0])
print (my_tuple[3])
print (my_tuple[-1])
print (my_tuple[-4])
# print (my_tuple[4])  IndexError
print (my_tuple[-1])
print (my_tuple[-4])

print (my_tuple.count('Edilson'))
print (my_tuple.index('Gomez'))

# La tupla es inmutable no se le puede cambiar el valor a uno de sus datos ni siquiera agregar de los que ya estan definidos.
# my_tuple [0] = 21 'tuple' object does not support item assignment

my_sum_tuple = (my_tuple + my_other_tuple)
print (my_sum_tuple)

print(my_sum_tuple [1:3])

# Cambiar el tipo de dato de tuple a list

my_tuple = list(my_tuple)
print(type(my_tuple))

# my_tuple_anadido = my_tuple.insert(0, 'Gomez') None
print(my_tuple)
my_tuple [0] = 'Torrado'
print(my_tuple)
# print(my_tuple_anadido)

my_tuple.insert(0, 'Torrado')
print(my_tuple)
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))
del my_tuple
# del my_tuple [2] TypeError: "tuple" object doesn't support item deletion
# print(my_tuple) NameError: name "my_tuple" is not defined