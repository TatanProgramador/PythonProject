
### Exceptions Handling ###

numberOne = 5
numberTwo = 1
numberOne = "1"

# try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido ningun error")
except:
    #Se ejecuta si se produce una excepcion
    print("Se ha producido un error")

# try except else

try:
    print(numberOne + numberTwo)
    print("No se ha producido ningun error")
except:
    print("Se ha producido un error")

else: #Opcional
    print("La ejecucion continua correctamente")

finally: # Opcional
    # Se ejecuta siempre pase lo que pase
    print("La ejecucion continua")

# Exceptiones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido ningun error")
except ValueError:
    print("Se ha producido un error ValueError")
except TypeError:
    #Se ejecuta si se produce una excepcion
    print("Se ha producido un error TypeError")

# Captura de la informacion del error

try:
    print(numberOne + numberTwo)
    print("No se ha producido ningun error")
except TypeError as error:
    print(error)
except Exception as error:
    print(error)