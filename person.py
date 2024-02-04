import config

def person():
    if config.lives >= 6: 
        print('|')
        print('|')
        print('|')
    elif config.lives == 5:
        print('|      O')
        print('|')
        print('|')
    elif config.lives == 4:
        print('|      O')
        print('|      | ')
        print('|')
    elif config.lives == 3:
        print('|      O')
        print('|     /| ')
        print('|')
    elif config.lives == 2:
        print('|      O')
        print('|     /|\\')
        print('|')
    elif config.lives == 1:
        print('|      O')
        print('|     /|\\')
        print('|     /  ')
    elif config.lives <= 0:       
        print('|      O')
        print('|     /|\\')
        print('|     / \\')

def draw():
    print('________')
    print('|      |')
    person()
    print('|_______')
