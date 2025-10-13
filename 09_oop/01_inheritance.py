class Car:
	def __init__(self):
		self.wheels = 4

class Jet:
	def __init__(self):
		self.wings = 2

class JetCar(Jet, Car):
	def __init__(self):
		Car.__init__(self)
		Jet.__init__(self)
	
	def calc(self):
		return self.wings + self.wheels

jc = JetCar()

print(jc.__dict__)
