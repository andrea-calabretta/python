# La lambda function è una funzione che non ha la parola chiave "def" ma al suo posto ci sarà la parola chiave "lambda" e inoltre la funzione lambda è caratterizzata dal fatto di non avere la parola chiave return

#invece di fare così:
def f(x):
	return x**2

print(f(8))

# faccio così:

square = lambda x: x**2
print(square(8))

# map(function, sequence)  applica la funzione function ad ogni elemento della sequenza e ritorna il risultato all'interno di una lista

for x in map(square, range(0,10)):
	print(x)

# possiamo anche fare tutto al volo, definire la funzione da applicare alla sequenza
for x in map( lambda x: x**3, range(0,11)):
	print(x)
