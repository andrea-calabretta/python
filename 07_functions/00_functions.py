def print_greeting():
	print("hello")
	print("my friend")

print_greeting()

# una funzione può ritornare o un solo valore o più valori (tramite una tupla) se più valori vengono compattati all'interno di una tupla stiamo utilizzando il meccanismo di packing
def funzione():
	return 1,2,3,4

x = funzione()
print(type(x))

# Posso associare le componenenti della tupla a delle variabili singola (unpacking = spacchettamento), ma devo sapere esattamente da quanti componenti è fatta quella tupla

c1, c2, c3 , c4 = funzione()
print(c1," ", c2, " " , c3, " ", c4)

# default parameters, con passaggio dei parametri posizionale
def divide( a , b = 2):
	return a/b

print(divide(4))

# passaggio dei parametri con asterisco, ovvero tramite una tupla
def asterik(*t):
	l1 = [x for x in t ]
	print( l1) 

t1 = ("pane", "vino", "pedalino")
asterik(*t1)


# passaggio dei parametri con doppio asterisco, ovvero tramite dizionario, quando passo gli argomenti con coppia chiave-valore non ho bisogno che venga rispettata la posizione\
d1 = { 'a' : 1, 'b' : 1, 'c' : 1 } #dizionario

def print_dict( **d):
	print(d.items()) 

print_dict(**d1)
