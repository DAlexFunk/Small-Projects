def checkRows(array, letter):
    if [letter,letter,letter] in array:
        return letter   #WE HAVE A WINNER

def checkColumns(array, letter):
    anXInEachRow = 0
    indexesSetX = []
    for i in array:
        if letter in i:
            anXInEachRow += 1

    if anXInEachRow >= 3:
        for a in range(3):
            for c,d in enumerate(array[a]):
                if d == letter:
                    indexesSetX.append(c)
#        print(indexesSetX)
        for checkLetter in range(3):
            if indexesSetX.count(checkLetter) >= 3:
                return letter    #WE HAVE A WINNER

def checkDiagonals(array, letter):
    if (array[0][0] == letter) and (array[1][1] == letter) and (array[2][2] == letter):
        return letter
    if (array[0][2] == letter) and (array[1][1] == letter) and (array[2][0] == letter):
        return letter

def checkAll(array):
    winner = None
    for letter in 'xo':
        if winner == None:
            winner = checkRows(array, letter)
        if winner == None:
            winner = checkColumns(array, letter)
        if winner == None:
            winner = checkDiagonals(array, letter)
        
        if winner != None:
            break
    return winner