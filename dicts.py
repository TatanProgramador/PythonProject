### Dictionarie ###
from sets import my_other_set

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre" : "Edilson" , "Apellido" : "Gomez", "Edad " : 18, "Altura" : "1.80" , 1 : "Python"}

my_dict = {
    "Nombre" : "Edilson" ,
    "Apellido" : "Gomez",
    "Edad " : 18,
    "Altura" : 1.80 ,
    1 : {"Python", "Java", "Ruby", "PHP"}
}

print(my_other_dict)
print(my_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict ["Nombre"])
my_dict ["Nombre"] = "Fabian"

print(my_dict)
print(my_dict["Nombre"])

my_dict ["Calle"] = "Cr 8 9 - 42"
print(my_dict)

del my_dict["Nombre"]
print(my_dict)
print("Nombre" in my_dict)


print(my_dict.items())
print(my_dict.values())
print(my_dict.keys())
print(my_dict.fromkeys(("Nombre", 1, "Apellido", "Edad", "Altura"))) #Se crea un nuevo diccionario sin valores