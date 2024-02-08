import config
import tttLogic
import random

conversion = {
    'a':0,
    'b':1,
    'c':2
}
possibleMoves = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']

def replace(List, index1, index2, replacer):
    List[index1].insert(index2, replacer)
    List[index1].pop(index2 + 1)
    return List


def getSquareInput(letter):
    #input must be in the form of 'LetterNumber' as in 'a1' or 'b3'. Colloums are letters, rows are numbers (like chess).  Indices start at a and 1
    while True:
        squareInput = input(f'Enter which position you would like to put your {letter}: ').lower().strip()
        if len(squareInput) != 2:
            print('Please enter a number in the right form (a2, b1, c3...)')
            continue
        if squareInput[0].isalpha() != True:
            print('Please enter a number in the right form (a2, b1, c3...)')
            continue
        if ('a' <= squareInput[0] <= 'c') != True:
            print('Please enter a number in the right form (a2, b1, c3...)')
            continue
        if squareInput[1].isnumeric() != True:
            print('Please enter a number in the right form (a2, b1, c3...)')
            continue
        if (1 <= int(squareInput[1]) <= 3) != True:
            print('Please enter a number in the right form (a2, b1, c3...)')
            continue
        if (squareInput in possibleMoves) == False:
            print('Move already played, choose another')
            continue
        break
    return squareInput

def getPlayerLetterChoice():
    while True:    
        playerLeterChoice = input('Would you like to be x or o?: ').lower().strip()
        if (playerLeterChoice != 'x') and (playerLeterChoice != 'o'):
            print('Please enter either x or o')
        else:
            break
    return playerLeterChoice

def robotsTurn(letter):
    if possibleMoves == []:
        return 0
    squareInput = random.choice(possibleMoves)
    replace(config.gameArray, int(squareInput[1]) - 1, conversion[squareInput[0]], letter)
    possibleMoves.remove(squareInput)


def playersTurn(letter):
    print()
    for i,j in enumerate(config.gameArray):
        print(f'{i+1}   {j[0]} | {j[1]} | {j[2]}')
        if i < 2:
            print(f"{'-'*9:>13}")
    else:
        print(f'\n    a   b   c')
    squareInput = getSquareInput(letter)
    replace(config.gameArray, int(squareInput[1]) - 1, conversion[squareInput[0]], letter)
    possibleMoves.remove(squareInput)


def main():
    winner = None
    playerLeterChoice = getPlayerLetterChoice()
    if playerLeterChoice == 'x':
        while winner == None:
            playersTurn('x')
            robotsTurn('o')
            winner = tttLogic.checkAll(config.gameArray)
            if possibleMoves == [] and winner == None:
                winner = 'Tie'
    else:
        while winner == None:
            robotsTurn('x')
            playersTurn('o')
            winner = tttLogic.checkAll(config.gameArray)
            if possibleMoves == [] and winner == None:
                winner = 'Tie'
            
    
    return winner, playerLeterChoice

gameOver = False
while not gameOver:
    winner, playerLetter= main()

    if winner == playerLetter:
        print('You Won!')
    elif winner == 'Tie':
        print('It was a Tie!')
    else:
        print('You Lost')
    
    gameOver = True