x = 1
num = []
sum = 0
while True:
    if x <=1000:
        num.append(str(x))
        x+=1
    else:
        break

for x in num:
    sum += int(x)

print(sum)