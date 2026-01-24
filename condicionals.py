### Conditionals ###
from operadores_logicos import my_string

my_conditions = 5 * 5

if my_conditions ==  10 :

    print("Se ejecuta la condicion del segundo if")

if my_conditions > 10 and my_conditions < 20 :
    print("El numero es mayor que 10 y menor que 20")

elif my_conditions == 25 :
    print("Es igual a 25")

else:
    print("El numero es menor o igual que 10 o mayor o igual que 20" ) # Me estaria esjecutando este print
# por que esat por fuera del else no esta pegado a la pared y no tiene tabulacion por lo cual me indica que esta por fuera del else


print("La ejecución continua")

my_string = ""

if my_string :
    print("Mi cadena de texto no esta vacia")

else :
    print("Mi cadena de texto esta vacia")  