# ==============================================================================
# ÍNDICE REFACTORIZADO: FUNDAMENTOS DE DATOS Y OPERACIONES EN PROGRAMACIÓN
# La información de texto proviene de los comentarios y el contenido de las fuentes.
# ==============================================================================

# 1. OPERACIONES ARITMÉTICAS BÁSICAS
# Esta sección cubre las operaciones matemáticas fundamentales utilizando variables enteras.

a = 3 # [1]
b = 4 # [1]

# Suma: Realiza la adición de los valores.
suma = a + b
print(f"Suma: {suma}") # [1]

# Resta: Realiza la sustracción.
print(f"Resta: {a - b}") # [1]

# Multiplicación: Realiza la multiplicación.
print(f"Multiplicacion: {a * b}") # [1]

# División: Realiza la división (resultado flotante).
print(f"Divicion: {a / b}") # [1]

# Módulo (%): Calcula el residuo de la división.
# Por ejemplo, el módulo de 3/4 da 3, ya que 3 no es divisible entre 4 y queda como residuo el número completo [1].
print(f"Modulo: {a % b}") # [1]

# Exponencial (**): Multiplica un número por sí mismo la cantidad de veces especificada por el exponente.
# Ejemplo: 5 ** 4 es 5 * 5 * 5 * 5 = 625 [1].
print(f"Exponencial: {5 ** 4}") # [1]


# 2. TIPOS DE DATOS PRIMITIVOS Y VERIFICACIÓN
# La función type() permite identificar el tipo de dato.

# Entero (Integer): Resultado de operaciones que no generan decimales.
print(type(3 + 5)) # Entero [1]

# Flotante (Float): Números con punto decimal.
print(type(3.14)) # Float [2]

# String (Cadena de caracteres).
print(type('El exito nos espera')) # String [2]

# 2.2. Números Complejos
# Los números complejos tienen una parte real y una imaginaria, representada con 'j' [2].
print(type(3j + 4j)) # [2]

# Para que el print funcione bien y me realice la operación, el número real debe ir primero [2].
print(f"Numero Complejo {3 + 4j}")# Complejo [2]

z = 7j + 4j # [2]
print(f"Numero Complejo (No suma, No concatena): {z}") # [2]
print(type(z)) # [2]

# Propiedades para acceder a las partes del número complejo.
print(f"Numero real: {z.real}") # [2]
print(f"Numero imaginario: {z.imag}") # [2]

a_complex = 4j # [2]
b_complex = 7j # [2]
c_real = 12 # [2]

# Comportamiento: Si se suman números complejos con un número real, el resultado es un nuevo número complejo.
# No los está sumando ni concatenando, solo está creando un número nuevo a partir de esa operación [2].
# Se debe ir primero el número sin la letra (la parte real) [3].
print(f"Operación con complejo y real (Primero el número real): {a_complex + b_complex + c_real}" ) # [2]


# 3. ESTRUCTURAS DE DATOS DE COLECCIÓN

# 3.1. Listas (list)
# Las listas son mutables y permiten almacenar diferentes tipos de datos.
# Hay que diferenciarlas bien, ya que se suelen confundir con las otras formas de almacenar datos que usan {} y () [3].
my_list = ["Edilson", "Fabian", "Gomez", "Torrado", 12] # [3]

# Modificación: Insertar un elemento (Mutabilidad).
my_list.insert(0, 13) # [3]

print(f"My List: {my_list}") # [3]
print(type(my_list)) # [3]

# Acceso por índice.
print(f"My List [4]: {my_list[4]}") # [3]
print(f"My list [1]: {my_list[1]}") # [3]
print(f"My list [2]: {my_list[2]}") # [3]

# 3.2. Diccionarios (dict)
# Almacenan datos en pares clave: valor [3].
# Solo es posible acceder solo con la clave; no es posible acceder con el valor ni con la posición [3].
# Python guarda los diccionarios en desorden y nunca los mostrará por posición, ya que no están en un orden específico [3].
my_dict = {"Name": "John", "Age": 18, 1.80 : "altura", "Lenguaje" : "Python"} # [3]
my_other_dict = {"Norte de Santander" : "Cucúta" , "Santander" : "Bucaramanga", "Atlantico" : "Barranquilla"} # [4]

print(f"Diccionario my_dict: {my_dict}") # [4]
print(f"My other list: {my_other_dict}") # [4]
print(type(my_dict)) # [4]

# Acceso mediante clave (1.80).
print(f"My dict clave 1.80: {my_dict[1.80]}") # [4]

# Métodos para ver claves y valores.
print(my_dict.keys()) # [5]
print(my_dict.values()) # [5]
print(type(my_dict)) # [5]
# print(my_dict[1]) # Este código fue comentado en la fuente para ilustrar el intento de acceso por posición o valor [4].

# 3.3. Conjuntos (set)
# El set no permite guardar datos repetidos; los duplicados son eliminados [4].
my_set = {9, 9, 1, 2, 2.3, 2.3, "Fabian", "Fabian", "Edilson"} # [4]
print(f"My set (Datos únicos): {my_set}") # [4]
print(type(my_set)) # [4]

# Ejemplo comparando sintaxis de diccionario (a) y conjunto (b).
a_dict = {1 : 1, 2 : 2, 3 : 3} # Diccionario [4]
b_set = {1 , 1, 2, 2, 3 ,4} # Conjunto [4]

print(a_dict) # [5]
print(b_set) # [5]
print(type(a_dict)) # [5]
print(type(b_set)) # [5]

# 3.4. Tuplas (tuple)
# La tupla es inmutable [5].
# Solo se podrán tener los datos ya agregados en la creación y no se podrá modificar después [5].
my_tuple = (1,"Edilson", 2, 3, 4, 5, 6) # [5]
print(f"My tuple {my_tuple}") # [5]


# 4. TIPOS DE DATOS BOOLEANOS (bool)
# Representan valores de verdad (True o False).

# Resultado de comparaciones lógicas.
my_bool_comparison_1 = 3==3 # [5]
print(f"My bool (3==3): {my_bool_comparison_1}") # [5]

# Asignación directa del valor False.
my_bool_false = False # [5]
print(f"My bool (False): {my_bool_false}") # [5]

# Otra comparación lógica.
my_bool_comparison_2 = 3 >= 2 # [5]
print(f"My other bool (3>=2): {my_bool_comparison_2}") # [5]