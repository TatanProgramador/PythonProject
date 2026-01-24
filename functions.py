

### Functions ###

def my_function():
    print("Mi cadena de texto esta vacia")

my_function()
my_function()
my_function()
my_function()


def sum_two_values(first, second):
    print(first + second)

# num1 = int(input("Ingresa un numero: "))
# num2 = int(input("Ingresa otro numero: "))

# sum_two_values(num1 , num2)

def sum_two_values_with_return(first, second):
    return first + second

my_result = sum_two_values_with_return(20 , 20)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname="John", name="Smith")

def print_name_with_defaulth (name, surename, aliase= "sin alias"):
    print(f"{name} {surename} {aliase}")

print_name_with_defaulth("John", "Smith")

def print_text (*texts):
    for text in texts:
        print(text.upper())

print_text("Hello", "World")