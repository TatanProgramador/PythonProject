

### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Edilson", "Gomez", 28, 1.80}
print(type(my_other_set))

print(my_other_set)
print(len(my_other_set))

my_other_set.add("Morado")
print(my_other_set) # Un Set es donde se almacenan natos pero en desorden y no se puede acceder a un datos en especifíco
# sino a todos en conjunto, y añadido a eso se elminan los datos duplicados

my_other_set.add("Morado")
print(my_other_set)

print("Morado" in my_other_set)
print("Verde" in my_other_set)

print(my_other_set)

my_other_set.remove("Morado")
print(my_other_set)
print(my_other_set)
print(my_other_set)
print(my_other_set)
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

del my_other_set
#print(my_other_set)  NameError: name 'my_other_set' is not defined

my_set = {1, 2, 3}
my_list_set = list(my_set)
print(my_list_set)
print(type(my_list_set))
print(my_list_set [0])
print(my_list_set [1])
print(my_list_set [2])

my_other_set = {"Java", "Python", "Ruby", "PHP"}

my_new_set = my_other_set.union(my_set)
print(my_new_set)
print(my_other_set.union(my_other_set).union({"JavaScrip", "C#"}))

print(my_new_set.difference(my_other_set))