from random import randint

player = 50

while True:
    coin = randint(1, 2)
    if player <= 0 or player >= 100:
        break
    else:   
        if coin is 1:
            player = player + 9
        else: 
            player = player - 10
if player <= 0:
    print("플레이어가 돈을 모두 잃었습니다")
else:
    print("플레이어가 100$를 땃습니다") 