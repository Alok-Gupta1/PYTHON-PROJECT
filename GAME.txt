import random
game=['snake' , 'water' , 'gun']
rounds=int(input('enter the number of rounds'))
pr=0
p=0
for i in range(rounds):
    pc=random.choice(game)
    player=input('ENTER EITHER SNAKE , WATER , GUN ')
    print(pc)
    if pc == player:
        print('DRAW')
    elif pc == 'snake' and player == 'water':
        print('YOU LOSE')
        p+=1
    elif player == 'snake' and pc == 'water':
        print('YOU WON')
        pr+=1
    elif pc == 'snake' and player == 'gun':
        print('YOU WON')
        pr+=1
    elif player == 'snake' and pc == 'gun':
        print('YOU LOSE')
        p+=1
    elif pc == 'water' and player == 'gun':
        print('YOU LOSE')
        p+=1
    elif player == 'water' and pc == 'gun':
        print('YOU WON')
        pr+=1
print()        
if p > pr:
    print('YOU LOSE THE GAME')
elif pr > p:
    print('YOU WON THE GAME')
else:
    print('GAME DRAW')
print('GAME OVER')    
        
