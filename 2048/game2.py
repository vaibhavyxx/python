#uses numbers to make 2048 game instead of oop
#use two matrices to do this game
import numpy as np
import random

#sets up the game with 2 random two
N=4
game = np.zeros((N,N))

print('Welcome to 2048!')
print('Press w, a, s, d to move tiles up, left, down and right')
print('Enter exit to quit the game')

#to populate a 2 at the game's random index
def populate2(countMax):
    count =0
    while(count <countMax):
        i = random.randrange(0, N)
        j = random.randrange(0, N)
        if(game[i,j] == 0):
            game[i,j] =2
            count+=1

#moves tiles upward
def moveUp():
    global game
    copyGame = np.zeros((4,4), dtype=int)  # Initialize a copy of the game board

    for i in range(N):
        lowerEmptyIndex = 0  # Start at the bottom of the column
        for j in range(N):
            if game[j, i] != 0:
                while lowerEmptyIndex < N - 1 and copyGame[lowerEmptyIndex, i] != 0:
                    lowerEmptyIndex += 1
                copyGame[lowerEmptyIndex, i] = game[j, i]
                if lowerEmptyIndex < N - 1:
                    lowerEmptyIndex += 1

    # After constructing copyGame, update the global game state
    game = copyGame.copy()
    return copyGame

#moves tiles downwards
def moveDown():
    global game
    copyGame = np.zeros((4,4), dtype=int)  # Initialize a copy of the game board

    for i in range(N):
        highestEmptyIndex = 3  # Start at the bottom of the column
        for j in range(N):
            if game[j, i] != 0:
                while highestEmptyIndex > 0 and copyGame[highestEmptyIndex, i] != 0:
                    highestEmptyIndex -= 1
                copyGame[highestEmptyIndex, i] = game[j, i]
                if highestEmptyIndex > 0:
                    highestEmptyIndex -= 1
    game = copyGame.copy()
    return copyGame

#moves tiles rightwards
def moveRight():
    global game
    copyGame = np.zeros((4,4), dtype=int)  # Initialize a copy of the game board

    for i in range(N):
        rightMostEmptyIndex = 3  # Start at the bottom of the column
        for j in range(N):
            if game[j, i] != 0:
                while rightMostEmptyIndex > 0 and copyGame[j, rightMostEmptyIndex] != 0:
                    rightMostEmptyIndex -= 1
                copyGame[j, rightMostEmptyIndex] = game[j, i]
                if rightMostEmptyIndex > 0:
                    rightMostEmptyIndex -= 1
    game = copyGame.copy()
    return copyGame

#moves tiles leftwards
def moveLeft():
    global game
    copyGame = np.zeros((4,4), dtype=int)  # Initialize a copy of the game board

    for i in range(N):
        leftMostEmptyIndex = 0  # Start at the bottom of the column
        for j in range(N):
            if game[j, i] != 0:
                while leftMostEmptyIndex < N-1 and copyGame[j, leftMostEmptyIndex] != 0:
                    leftMostEmptyIndex += 1
                copyGame[j, leftMostEmptyIndex] = game[j, i]
                if leftMostEmptyIndex > 0:
                   leftMostEmptyIndex += 1
    game = copyGame.copy()
    return copyGame

populate2(2)
print(game)

userInput = ''
highestSum =0
#some bug 
while(userInput != 'exit' or highestSum == 2048):
    userInput = input('Enter your move: ')
    if(userInput == 'w'):
        game = moveUp()
    elif (userInput == 's'):
        game = moveDown()
    elif(userInput == 'd'):
        game = moveRight()
    elif(userInput == 'a'):
        game = moveLeft()

    populate2(1)
    print(game)

if(userInput == 'exit'):
    print('Game exited')