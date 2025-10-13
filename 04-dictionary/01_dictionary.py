"""
 il dizionario è un hash table pochè ogni elemento è caratterizzato dall'avere una chiave e un valore associato.
 L'accesso ad ogni elemento  è basato sull'utilizzo della chiave.
Il dizionario può essere modificato e possono essere aggiunte e modificate coppie del nostro dizionario.

"""

d1 = {}
d2 = dict()

d3 = { "Name" : "Susan", "Age": 19, "Major": "CS" }
d4 = dict(Name = "Susan", Age = 19, Major = "CS")
d5 = dict(zip(['Name','Age','Major'],["Susan", 19, "CS"]))
d6 = dict([('Age', 19), ('Name', "Susan"), ('Major', "CS")])

print(d1)
print(d3)
print(d4)
print(d5)
print(d6)

# accedere ad uno specifico elemento:
print(d3['Age'])

# cancellare uno specifico elemento:
del d3['Age']
print(d3)

# cancellare tutti gli elementi:
d3.clear()
print(d3)
