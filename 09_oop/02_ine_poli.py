class Person:
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
	def toString(self):
		return self.name + " " + self.surname

class Student(Person):
	def __init__(self, name, surname, matr):
		Person.__init__(self,name, surname)
		self.matr = matr
	def toString(self):
		return Person.toString(self) + " matric. : "+ self.matr

class Worker(Person):
	def __init__(self, name, surname, salary):
		Person.__init__(self, name, surname)
		self.salary = salary
	def toString(self):
		return Person.toString(self)+ " " +self.salary

class StudentWorker(Student, Worker):
	def __init__(self, name, surname, salary, matr):
		Student.__init__(self,name, surname, matr)
		self.salary = salary



p = Person("Pinco", "Pallino")
print(p.toString())

s = Student("Mario", "Rossi", "000")
print(s.toString())

w = Worker("Ignazio", "Bianchi", "soldi a palate")
print(w.toString())

sw = StudentWorker("Andrea", "Calabretta", "111", "quanto basta")

print(sw.toString())
