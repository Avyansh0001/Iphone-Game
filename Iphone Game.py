from random import randint
print('Iphone XII Pro Max Game')
feeling_brave=True
score=0
while feeling_brave:
    ghost_door = randint(1, 3)
    print('Three doors ahead')
    print('Iphone XII Pro Max is behind one of these three doors.')
    print('Which door do you open?')
    door = input('1, 2, or 3?')
    door_num = int(door)
    if door_num == ghost_door:
        print('Iphone XII Pro Max!')
        feeling_brave = False
    else:
        print('No Iphone !')
        print('Y0u enter the next room.')
        score = score + 1
print('Congratulations!!! U have found the Iphone XII Pro Max but not in RL...LOL')
print('Game over! You scored', score)