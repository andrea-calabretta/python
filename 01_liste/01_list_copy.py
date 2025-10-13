mylist1 = [] # create an empty list
print(mylist1)

mylist2 = [12, 33, "stringa"] # list can collect different datype
print(mylist2)

mylist3 = [x for x in range(1,10)]  #list comprehnsion
print(mylist3)

mylist4 = list() # other way to create an ampty list
print(mylist4)

l5 = list([ 2, 4, 5, 6])
print(l5)

l2 = l5 #è una copia dei riferimenti, quindi se cambio una delle due lista, cambia automaticamente anche l'altra

l6 = list(l5) # copia solo dei valori quindi se cambio una delle liste l'altra resta invariata

l5.append(99)

print("l2 :", l2)
print("l5 :", l5)
print("l6 :", l6)

