somme1 = 0
somme2 = 0

for i in range(101):
    somme1 = i*i + somme1

for i in range (101):
    somme2 = somme2 + i
somme2 = somme2 * somme2

print(somme2 - somme1)