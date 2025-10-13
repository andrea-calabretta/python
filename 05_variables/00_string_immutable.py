phrase = "stringa uno"
print("phrase = " + phrase)
print("Address of phrase is: {}".format(id(phrase)))

#riassegno il valore a phrase e vedo che l'indirizzo di memoria è diverso
phrase = "stringa due"
print("phrase = " + phrase)
print("Address of phrase is: {}".format(id(phrase)))

print("\nLe stringhe sono immutabili, quindi quando facciamo una riassegnazione ad una stringa, in realtà non sovrascriviamo lo stesso indirizzo di memoria  ma facciamo in modo che quella variabile (che in realtà è un riferimento) punti ad un'altro indirizzo di memoria")
