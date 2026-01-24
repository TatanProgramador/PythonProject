

### Clases ###

class  MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
my_person = Person("Edilson", "Fabian")
print(f"{my_person.name}, {my_person.surname}")

class Person:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}" # Esta propiedad es publica
        self.__name = name # Esta propiedad con __ es privada
        self.__surname = surname

    def get_name (self):
        return self.__name

    def studing (self):
        return f"{self.full_name} está estudiando"

    def leguaje (self):
        return f"{self.full_name} el lenguaje de Python"

    def studing_language(self):
        print(f"{self.studing()} el lenguaje de Python")

my_person = Person("Edilson", "Fabian")
print(my_person.full_name)
print(my_person.get_name())
my_person.studing()
my_person.studing_language()