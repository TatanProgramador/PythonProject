from dicts import my_dict

### Loops ###

# While

my_conditions = 0

while my_conditions < 10:
    print(my_conditions)

    my_conditions += 2
else:
    print("Mi condición es mayor o igual que 10")

print("La condición continua")

while my_conditions < 20:
    my_conditions += 1
    if my_conditions == 15:
        print("Se detiene la ejecucion con el valor 15")
        break

    print(my_conditions)

print("La ejecucion continua")

my_list = [35, 24, 64, 67, 24, 10]

for element in my_list:
    print(element)

my_tuple = (35, 24, 64, 67, 24, "Edilson", "Gomez", 1.80)

for element in my_tuple:
    print(element)

my_set = {"Edilson", "Fabian", "Morado", 1.80}
for element in my_set:
    print(element)

my_dict = {"Nombre": "Edilson", "Apellido":"Gomez" , "Edad": 20, "Color" : "Morado"}
for element in list(my_dict.values()):
    print(element)
    if element == 20:
        break
else:
    print("El bucle for para el diccionario ha finalizado")


print("La ejecucion continua")



