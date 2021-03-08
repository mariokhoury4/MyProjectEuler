
Dict = {}

def chain(x):
    temp = x
    n = 0 
    while x != 1:
        if x % 2 == 0 :
            x = x/2
            if x in Dict.keys():
                n = n + Dict[x]
                break
        else:
            x = 3*x + 1
            if x in Dict.keys():
                n = n + Dict[x]
                break
        n = n + 1
    Dict[temp] = n
    return n

Max = 0
index = 0
for i in range(1,1000000):
    temp = chain(i)

    if (temp>Max):
        Max = temp
        index = i
print(index)