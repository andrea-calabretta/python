#L'operatore + permette di fare somme e  concatenare stringhe ma non di oggetti, ma io posso fare overloading e concatenare oggetti

class A:
	def __init__(self, a):
		self.a = a
	
	def __add__(self, o):
		return self.a + o.a

ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)
