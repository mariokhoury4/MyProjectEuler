num1 = 1
num2 = 2
MAX = 4000000
result = 2

def is_Even(x):
    if (x % 2 == 0):
        return True
    return False

while True:
    num1 = num1 + num2
    if (num1 >= MAX):
        break
    if is_Even(num1):
        result = result + num1

    num2 = num2 + num1
    if(num2 >= MAX):
        break
    if is_Even(num2):
        result = result + num2

print(result)
