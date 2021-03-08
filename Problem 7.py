import math
def is_Prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if (x % i == 0):
            return False
    return True

counter = 1

for i in range(3,999999999):
    if is_Prime(i):
        counter = counter + 1
    if counter == 10001:
        print(i)
        break