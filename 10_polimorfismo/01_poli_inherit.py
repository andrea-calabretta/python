# Applichiamo il polimorfismo utilizzando il concetto di ereditarietà
# pytho utilizza sempre il binding dinamico quindi c'è sempre polimorfismo

class Bird:
	def intro(self):
		return "There are many types of birds."

	def flight(self):
		return "Most of the birds can fly nut some cannot."


class Sparrow:
	def flight(self):
		return "Sparrows can fly."

class Ostrich(Bird):
	def flight(self):
		return "Ostriches cannot fly."

b = Bird()
s = Sparrow()
o = Ostrich ()

print(b.flight())
print(s.flight())
print(o.flight())

