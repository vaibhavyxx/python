#methods are declared on top in python- to draw hangman
def drawsHangman(attemptsLeft):
    if(attemptsLeft >=6):
        print(' ______')
        print('|     ')
        print('|     ')
        print('|     ')
        print('|     ')

    elif(attemptsLeft == 5):
        print(' ______')
        print('|   |  ')
        print('|   o  ')
        print('|     ')
        print('|     ')

    elif(attemptsLeft ==4):
        print(' ______')
        print('|   |  ')
        print('|   o  ')
        print('|  /   ')
        print('|     ')

    elif(attemptsLeft ==3):
        print(' ______')
        print('|   |  ')
        print('|   o  ')
        print('|  /|   ')
        print('|     ')

    elif(attemptsLeft ==2):
        print(' ______')
        print('|   |  ')
        print('|   o  ')
        print('|  /|\\   ')
        print('|     ')

    elif(attemptsLeft ==1):
        print(' ______')
        print('|   |  ')
        print('|   o  ')
        print('|  /|\\   ')
        print('|  /  ')
    
    else:
        print(' ______')
        print('|   |  ')
        print('|   o  ')
        print('|  /|\\   ')
        print('|  / \\ ')

#make a copy of word's list that the player will see and fill it up
word = 'bananas'
hidden = '------'
hiddenList = list(hidden)
wordList = list(word)
print(hidden)
print('Welcome to Hangman!')
attempts = 6
i=-6
dashCount = len(hidden)
#item reassignment not possible

while(attempts >= 0):
    print(f"guess the word: {hiddenList}")
    if(dashCount ==0): print("You have won!");break

    guess = input('enter a letter: ')

    i = word.find(guess)
    if(i == -1):
        attempts -=1
        #print('Wrong! You have ' +attempts+ ' attempts left')
    else:
        count =0
        #checks if that letter is present, yes then updates the correct guesses
        for letter in wordList:
            if(letter == guess):
               hiddenList[count] = guess; dashCount-=1
            count+=1
        #print(hiddenList)

    drawsHangman(attempts)        
    print(f"You have {attempts} attempts left")

print("You have lost")
    



    
    

