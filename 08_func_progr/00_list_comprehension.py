# list comphrension è un tipo di programmazione funzionale in cui una lista dati viene costruita attraverso l'utilizzo di una funzione inline che mi serve per calcolare i valori

squares = [ x**2 for x in range(0,11) ]
print(squares)

#creiamo una lista di tuple
compl = [( x, x**2, x**3) for x in range(0,13) if x % 2 == 0]
print(compl)

#list comprehension di list comprehension
innes = [[x*y for x in range(1,5)] for y in range(1,5)]
print(innes)
