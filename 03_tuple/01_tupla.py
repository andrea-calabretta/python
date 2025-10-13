# In una tupla, gli elementi possono essere di qualsiasi tipo, anche ripetuti (come nella lista) con l'unica differenza che la lista è mutabile mentre la tupla è IMMUTABILE

#si creano come le lista ma con le parentesi tonde () piuttosto che con le parentesi quadre

t1 = ()
t2 = (1, 2, 3, 'string')
print(t2)

#tuple packing
t = "susan", 19, "CS"
print(t)

#tuple unpacking
name, age , major = t
print ("name :", name)
print ("age :", age)
