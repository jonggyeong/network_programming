days = {'January':31, 'February':28, 'March':31, 'April':30,  
        'May':31, 'June':30, 'July':31, 'August':31,  
        'September':30, 'October':31, 'November':30, 'December':31}

user_input = input("write here: ")

for key in days:
    if key == user_input:
        print(days[key])

print( sorted(days.keys()), end='\n\n')

for key in days:
    if days[key] == 31:
        print(key, end=' | ')
print('\n\n')

Sortdays = sorted(days.items(), key=lambda t: t[1])
print(Sortdays)

user_input2 = input('write here: ')

if len(user_input2) == 3:
    for key in days:
        if user_input2 in key :
            print(days[key])
else:
    print('write 3 letters!')

