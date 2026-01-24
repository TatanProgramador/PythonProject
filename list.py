

# Listas

my_list = list()
my_other_list = []

print (len(my_list))

my_list = [12, 12, 63, 75, 78]
print (my_list)

my_other_list = [20, 1.80, "Edilson", "Gomez"]

print (my_other_list)
print (len(my_other_list))

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list.count("Edilson"))
my_other_list.append("Abrego")
my_other_list.insert(1, "Morado")
my_other_list.remove("Morado")
my_list.remove(12)#Me elimina el numro el cual le indique que este en la lista y si se repite el elemento se elimina el primero
print(my_list)
print(my_list.pop())
print(my_list)

del my_list[0]#Me elimina el indice de la posicion que le indique
print(my_list)

print(my_other_list)

my_other_list.reverse()
print(my_other_list)