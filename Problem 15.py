from math import factorial

def nck(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

print(str(nck(20+20,20)))  