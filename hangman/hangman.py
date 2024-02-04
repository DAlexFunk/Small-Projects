import random
import person
import config
import time

letters = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
numbers = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
words = {
    1:'extreme',
    2:'drama',
    3:'flex',
    4:'competence',
    5:'smile',
    6:'genetic',
    7:'tire',
    8:'plain',
    9:'freshman',
    10:'diet'
}

wordToBeGuessed = ''
lettersGuessed = set()
lettersInWord = set()
lettersInWordList = []
guessesResultSet = []

if __name__ == '__main__':
    while True:    #decide who is guessing
        whoIsGuesser = input('Would you like to be the guesser or the computer (enter "me" or "computer")?: ')
        if whoIsGuesser == 'me': break
        elif whoIsGuesser == 'computer': break
        else:
            print('please enter either "me" or "computer"')

    if whoIsGuesser == 'computer':   #computer is guessing
        wordToBeGuessed = input('Please enter a word to be guessed (only one word): ')
        lowerWord = wordToBeGuessed.lower()    
        for i in lowerWord:  #create the set for the word for comparison
            lettersInWord.add(numbers[i])
        while (config.lives > 0) and (lettersInWord.issubset(lettersGuessed) == False):  #computer is guessing
            letterGuessed = random.randint(1,26)
            letterInList = letterGuessed in lettersGuessed
            if letterInList == False:  #check if has been guessed before
                print(f'\nComputer guessed {letters[letterGuessed]}')
                if lowerWord.count(letters[letterGuessed]) == 0:
                    print(f'The letter {letters[letterGuessed]} is not in the word')
                    config.lives -= 1
                    lettersGuessed.add(letterGuessed)
                else:
                    print(f'The letter {letters[letterGuessed]} is in the word')
                    lettersGuessed.add(letterGuessed)
            time.sleep(1.5)
        if config.lives == 0:
            print(f'\nThe computer did not guess the word {wordToBeGuessed} and lost')
        else:
            print(f'\nThe computer guessed the word {wordToBeGuessed} and won')

    if whoIsGuesser == 'me':  #user is guesser
        wordToBeGuessed = words[random.randint(1,10)]   #generate word
#        for _ in range(random.randint(3,15)):
#           wordToBeGuessed += letters[random.randint(1,26)]
        for i in wordToBeGuessed:   #generate set for the word
            lettersInWord.add(numbers[i])
            lettersInWordList.append(numbers[i])
        for _ in wordToBeGuessed:  #make visual elelemt for user
            guessesResultSet.append('_')
        guessesResultString = ' '.join(guessesResultSet)
        while (config.lives > 0) and (lettersInWord.issubset(lettersGuessed) == False):  #actual game part
            person.draw()
#            print(wordToBeGuessed)
            print(f'\n{guessesResultString}')
            decision = input('Would you like to guess a letter or the word?: ')  #see if user wants to guess letter or word
            if decision == 'letter':
                letterGuessed = numbers[input('Please Guess a Letter (lowercase): ')]  #get the letter
                letterInList = letterGuessed in lettersGuessed
                if letterInList == False:  #make sure user has not already guessed the letter
                    if wordToBeGuessed.count(letters[letterGuessed]) == 0:  #check if letter is in word
                        print(f'The letter {letters[letterGuessed]} is not in the word')
                        config.lives -= 1
                        lettersGuessed.add(letterGuessed)
                    else:
                        print(f'The letter {letters[letterGuessed]} is in the word')
                        while lettersInWordList.count(letterGuessed) > 0:  #find the positions of the letter(s) and update visual accodinngly
                            index = lettersInWordList.index(letterGuessed)
                            guessesResultSet.insert(index, letters[letterGuessed])
                            guessesResultSet.pop(index + 1)
                            lettersInWordList.insert(index, -1)
                            lettersInWordList.pop(index + 1)
                        guessesResultString = ' '.join(guessesResultSet)
                        lettersGuessed.add(letterGuessed)
                else:
                    print(f'You have already guessed {letters[letterGuessed]}, please choose another letter')
            elif decision == 'word':
                wordGuessed = input('Enter a word (lowercase): ')
                if wordGuessed == wordToBeGuessed:
                    break
                else:
                    print(f'{wordGuessed} is not the word')
#                    config.lives = 0         #only allow correct guessed of the word.  Incorrect guesses of the full word means loss
            else:
                print(f'Input "{decision}" not recognized.  Please type either "letter" or "word"')
        if config.lives <= 0:
            person.draw()
            print(f'\nYou did not guess the word {wordToBeGuessed} and lost')
        else:
            print(f'\nYou guessed the word {wordToBeGuessed} and won!')