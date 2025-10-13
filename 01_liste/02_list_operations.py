lista = [ x for x in range(1,10) ]

lista[0] = "x"  #item 0 is replaced
print(lista)


lista = [ x for x in range(1,10) ]
lista[1:5] = "qwe" # slice from 1 to 5 is replaced
print(lista)


lista = [ x for x in range(1,10) ]
lista[1:5] = "sostituzione" # slice from 1 to 5 is replaced
print(lista)

lista = [ x for x in range(1,10) ]
del lista[1:5]
print(lista)

lista = [ x for x in range(1,10) ]
lista[0:9:2] = "sosti" # inizzio: fine: step
print(lista) 

del lista[0:9:2]
print(lista)
