""" il polimorfismo è indipendente dal meccanismo di ereditarietà nel senso che nel
momento in cui io definisco un oggetto, su oggetti diversi io potrò invocare metodi con lo stesso nome ma è possibile anche considerare un meccanismo di polimorfismo classico basato sull'ereditarietà """

class P1:
	def M1(self):
		return 5
class P2:
	def M1(self):
		return 1

x1 = P1()
x2 = P2()

t = [ x1, x2 ]

for x in t:
	print(x.M1())

# Invocando lo stesso metodo su classi diverse ho ottenuto polimorfismo anche se le classi non hanno alcun legame di ereditarietà
