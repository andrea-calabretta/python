# lista è una struttura di riferimenti ad elementi eterogenei ed è mutabile, e gli elementi possono essere ripetuti

mylist = [] # create an empty list

print(mylist)
print( "list address is {}".format(id(mylist)))
mylist = [ 12, 13, "stringa"]

print( "list address is {}".format(id(mylist)))
print(mylist)

mylist.append("coda")

print(mylist)

print( "list address is {}".format(id(mylist)))

l2 = list()

l3 = list ([2 , 3, 4 ,5])

# copiare i riferimenti della lista quindi la lista è la stessa puntata da riferimenti diversi, quindi se io faccio una modifica, la stessa modifica apparirà anche sull'altra lista

l4 = l3

print("l3:", l3)
print("l4:", l4)

l3.append("modifica")

print("l3:", l3)
print("l4:", l4)
#copiare solo il contenuto della lista ma sono due liste diverse, se io faccio una modifica, la modifica è solo su una delle due

l4 = list(l3)
l3.append("solo l3")

print("l3:", l3)
print("l4:", l4)
