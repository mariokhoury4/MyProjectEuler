words = ["One","Two", "Three", "Four","Five", "Six", "Seven", "Eight", "Nine", "Ten","Eleven", "Twelve","Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
decades = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]


for d in decades:
    words.append(d)
    for i in range(0,9):
        words.append(str(d + words[i]))

for j in range(0,9):
    words.append(str(words[j] + 'hundred'))
    for k in range(0,99):
        words.append(str(words[j]+'hundredand' + words[k]))
words.append('onethousand')
c = 0
for w in words:
    c = c + len(w)

print(c)