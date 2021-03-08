def is_palindrome(x):
    x = str(x)
    for i in range(int(len(x)/2)):
        if(x[i]!= x[len(x)-i-1]):
            return False
    return True

x = 999
find = False
res = []
while x>900:
    y=999
    while y>900:
        if(is_palindrome(x*y)):
            find = True
            res.append(x*y)
        y = y-1
    x = x - 1
print(max(res))
    