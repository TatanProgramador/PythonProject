

empaty_dict = dict()
print(type(empaty_dict))

primary_dict = {'Edilson': 56, 43 : 'Gomez'}

person = {'first_name' : 'Edilson',
          'last_name': 'Gomez',
          'age' : 20,
          'libraries': ('Numpy', 'Pandas', 67),
          'country' : 'Colombia',
          'is_marred' : True,
          'Skill' : ['Java' , 'Python', '.Net', 'Node'],
          'address' : {'street' : 'Space street', 'Zipcode' : '02210'
                       }
          }

print(len(person))

print(person.get('first_name'))
print(person.get('last_name'))
print(person.get('age'))
print(person.get('country'))
print(person.get('is_marred'))
print(person.get('Skill')[0])
print(person.get('address'))
print(person.get('address')['street'])
print(person.get('city'))
print(person['libraries'])


# El metodo get primero me comprueba de si exite esa clave y no me envia un TypeError si no que me envia un NoneType

person['city'] = 'Abrego'
person['Skill'].append('Ocaña') # Con append solo se le puede añadir mas valores a una lista, no se le puede ahrhar por ejemplo a algo qeu solo sea clave valor directamente.
#person['libraries'].append('Nump') Esto me da error ya que las tuplas son inmutables, no se pueden modificar. y aca le estoy agrgando un nuevo elemento despues de creada.
print(person['Skill'])
print(person['libraries'])
print(person)
person['first_name'] = 'Fabian'
print(person['first_name'])
print('first_name' in person.keys())
print('Colombia' in person.values())
print('Numpy' in person['libraries'])
person.pop('first_name')
print(person)
eliminado = person.popitem()
print(eliminado)
del person['Skill']
print(person)
print(type(person))
print(person.items()) # El metodo items cambia el diccionario a una lista de tuplas
print(person)
print(type(person))
#print(person.clear())
print(person)
print(type(person))
dtc_copy = person.copy()
print(dtc_copy)
keys = person.keys()
print(keys)
values = person.values()
print(values)