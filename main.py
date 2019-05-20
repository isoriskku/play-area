from playArea import *
from time import sleep

while(True):
    print()
    print('-----menu-----')
    print('1. insert play area')
    print('2. delete play area')
    print('3. show play area list')
    print('4. check play area')
    sel = int(input('select(-1 is exit): '))

    if(sel == -1):
        break
    
    elif(sel == 1):
        setPlayArea()

    elif(sel == 2):
        delPlayArea()

    elif(sel == 3):
        showPlayArea()

    elif(sel == 4):
        print(CheckArea(37.293891, 126.975474)) # GPS 값

    else:
        print('check your input')
