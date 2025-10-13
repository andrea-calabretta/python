class Person:
		_nome: "" # l'underscore impone visibilità privata agli attributi
		_cognome: ""
	def __init__(self, nome, cognome):
		self.name = nome
		self.surname = cognome

	def toString(self):
		return f'Person name is {self.name} and surname is {self.surname}'

andrea = Person("Andrea", "Calabretta")

print("__str__()")
print(andrea.__str__())

print(andrea.toString())
print(type(andrea))

print("__dict__")
print(andrea.__dict__)
print("__doc__")
print(andrea.__doc__)
# print(andrea.__name__)
print("__module__")
print(andrea.__module__)
print("__base__")
print(andrea.__bases__)
