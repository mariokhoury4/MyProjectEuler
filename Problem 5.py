num = [20,19,18,17,16,14,13,11]

for i  in range (2520,99999999999,2520):
    if all(i % n ==0 for n in num):
        print(i)
        break


