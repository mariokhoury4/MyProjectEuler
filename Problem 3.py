import math

NUMBER = 600851475143 

def is_Prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if (x % i == 0):
            return False
    return True

res = []
i = 2 
while True:
    if (NUMBER % i == 0):
        if(is_Prime(i)):
            res.append(i)
        NUMBER = int(NUMBER/i)
        i = 2
    else:
        i = i + 1
    if (NUMBER not in res):
        if(is_Prime(NUMBER)):
            res.append(NUMBER)
            break
print(max(res))
