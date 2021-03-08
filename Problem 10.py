import math
def is_Prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if(x % i ==0):
            return False
    return True

result = 2
for i in range(3,2000000):
    if is_Prime(i):
        result = result + i
print(result)