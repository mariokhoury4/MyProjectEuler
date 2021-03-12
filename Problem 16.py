s = 2
for i in range(1,1000):
    s = s *2
s = str(s)

result = 0
for i in s:
    result = int(i) + result
print(result)