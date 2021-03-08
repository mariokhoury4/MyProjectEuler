import math
number = 0 
i = 1

def nb_divisor(number):
    n = 0
    sqrt = int (math.sqrt(number))

    for i in range(1,sqrt+1):
        if number % i == 0:
            n = n + 2
    
    if sqrt*sqrt == number:
        n = n -1
    return n


while(nb_divisor(number) < 500):
    number +=i
    i = i + 1
print(number)

