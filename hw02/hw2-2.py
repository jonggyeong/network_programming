a = int(input('Number 1: '))
b = int(input('Number 2: '))

if a < b: 
    a, b = b, a   

while b != 0:
    a, b = b, a % b

print(a)   