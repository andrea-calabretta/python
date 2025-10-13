# for
print("primo ciclo")
for i in range(0,4): # min, max
	print(i)

print("secondo ciclo")
for i in range(0,10,2): #min, max, step
	print(i)

for x in "banana":
	print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

for x in [0, 1, 2]:
  pass # no operation, in order to avoid raised errors
# if 
a = 1
b = 0
c = 2
if a > b:
	if a > c:
		print ("a is the greatest")
	else:
		print("c is the greatest")
elif b > c:
		print(" b is the greatest")
else:
		print(" c is the greatest")

i = 1
while i <6:
	print(i)
	if(i == 3):
		print("siamo a 3")
	i += 1
