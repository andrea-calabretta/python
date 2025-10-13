# map(function, sequence)  applica la funzione function ad ogni eleme    nto della sequenza e ritorna il risultato all'interno di una lista
square = lambda x: x**2
print(square(8))

for x in map(square, range(0,10)):
	print(x)

# possiamo anche fare tutto al volo, definire la funzione da applicar    e alla sequenza

for x in map( lambda x: x**3, range(0,11)):
  print(x)

