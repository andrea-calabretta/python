""" reduce non fa altro che ottenere un unico valore a partire da una sequenza ottenuta applicando una funzione lambda al primo elemento della sequenza e poi combinando il risultato ottentuo al secondo elemento della sequenza sulla quale viene sempre applicata la funzione lambda e così via per tutti gli elementi della sequenza
"""
""" reduce(function, sequence) ritorna un singolo valore ottenuto come risultato dell'applicazione di una funzione ai primi due elementi di una sequenza, e poi combinandolo al risultato sull'elemento successivo (al quale viene sempre applicata la funzione) e così via """
import functools
#inizializzo la lista
lis = [1, 3, 5, 6, 2 ]

print("The sum of the list elements is: ", end ="")
print(functools.reduce(lambda a,b: a+b, lis))
