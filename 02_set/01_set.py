#in sets elements must be unique, elements replicated are not allowed (In list it's allowed")

basket = ['orange', 'apple', 'apple', 'orange']
fruit = set(basket)
print(fruit) # stampa solo 'orange' e 'apple' presi una volta sola

# l'operatore 'in' restituisce TRUE se un certo elemento è presente nel set, FALSE altrimenti

print('orange' in fruit) # TRUE

dish = [ 'lasagne', 'pizza', 'pizza', 'parmigiano']
kitchen = set(dish)
print(kitchen)

print(fruit | kitchen)

