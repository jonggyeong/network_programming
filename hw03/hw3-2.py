d=[{'name':'Todd', 'phone':'555-1414','email':'todd@mail.net'},
    {'name':'Helga', 'phone':'555-1618','email':'helga@mail.net'},
    {'name':'Princess', 'phone':'555-3141','email':''},
    {'name':'LJ', 'phone':'555-2718','email':'lj@mail.net'}]

for i in range(4):
    number =  d[i]['phone']
    if number[-1] == '8':
        print('전화번호가 8자로 끝나는 사용자:', d[i]['name'])
print('\n')

for i in range(4):
    email =  d[i]['email']
    if email == '':
        print('이메일이 없는 사용자:',d[i]['name'])
print('\n')

user_input = input('이름을 입력하세요!')
i=0
while True:
    if i==4:
        print('이름이 없습니다')
        break

    name = d[i]['name']
    if user_input == name:
        print('전화번호:',d[i]['phone'],','
            ,'이메일:',d[i]['email'])
        break
    else:
        i+=1