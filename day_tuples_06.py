from itertools import count

my_tuple = (1 , 2, 3, 4, 5, 'hsjdgh', [] )
print(type(my_tuple))
print(my_tuple)
print(my_tuple[6])
print(len(my_tuple))

fruits = ['apple', 'banana', 'orange', 'grape']
first_fruit = fruits[0]
print(first_fruit)
last_fruit = len(fruits) - 1
fruta = fruits[last_fruit]
print(fruta) ## orange
print(last_fruit)
first_fruit = fruits[-1]
print(first_fruit)
second_fruit = fruits[1:3:2]
print(second_fruit)

##Convertir una tupla a lista para poder modificarla

tpl = (1, 2, 3, 4, 5)
lst = list(tpl)
print(type(lst))
##lst.insert(2, 6)
print(lst)

print(1 in tpl)
print(2 in lst)
print(3 in lst)

tpl1 = (1, 2, 3, 4, 5)
tpl2 = (1, 2, 3, 4, 5)
union = tpl1 + tpl2
print(union)
del tpl1
