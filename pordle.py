# Name: Joshua Williams
# Program Purpose: Pordle (PVCC Wordle): Word Guessing Game
#   The program chooses a random word from a file of words. The user tries to
#   figure out the word in the fewest guesses by guessing letters in the word.
#   This program uses an input FILE, LISTS, and STRING SLICES (section of the string).

import random

def main():
    global wordList
    playAgain = True
    
    while playAgain:
        printHeadings()
        printMenu()
        
        wordList = [] #clears the list from the last play
        wordFile = open(inFile, "r") #open the file for READ
        for textLine in wordFile: #read in a line of text from the file
            for word in textLine.split(): #split the line of text into two words
                wordList.append(word) #add each word to the word list
        wordFile.close()

        playGame()            
        yesno = input("Would you like to play again? (Y/N) ")
        if yesno == "n" or yesno == "N":
            playAgain = False
            print("Thank you for playing PORDLE!")
            return()

def printHeadings():
    print("\nWelcome to PORDLE! The PVCC Wordle Game.")
    print("I will think of a word and you try to guess the letters in the word.")
    print("The number of dashes indicates the number of letters in the word.")

def printMenu():
    global inFile
    print("\nChoose a PORDLE category:")
    print("\t1. Animals")
    print("\t2. Cars")
    print("\t3. SPORTS")
    print("\t4. FOODS")

    category = input("Please enter the category number: ")
    
    if category == "1":
        inFile = 'animal.txt'
        print("\nThis will be an ANIMAL Pordle")
    elif category == "2":
        inFile = 'car.txt'
        print("\nThis will be a CAR Pordle")
    elif category == "3":
        inFile = 'sport.txt'
        print("\nThis will be a SPORTS Pordle")
    elif category == "4":
        inFile = 'food.txt'
        print("\nThis will be a FOOD Pordle")
    else:
            inFile = 'animals.txt'
            print("\nThis will be an ANIMAL Pordle")


def playGame():
    numGuesses = 1
    lettersUsed = []
        
    wordChosen = random.choice(wordList)
    pordle = wordChosen
    
    for i in range(len(pordle)):
        pordle = pordle[0:i] + "_" + pordle[i+1:] #Use SLICE to replace each letter with a '_'.
    print(" ".join(pordle)) #the "join" will put a space between each underscore

    while pordle != wordChosen: #keep asking the player until player guesses the word
        letterGuess = input("Please enter a letter: ")
        letterGuess = letterGuess.lower()
        lettersUsed.append(letterGuess) #Add the players' letter to the list of guessed letters
        print("Number of Guesses: " + str(numGuesses))

        for i in range(len(wordChosen)): #Search through the letters to find a match
            if wordChosen[i] == letterGuess:
                pordle = pordle[0:i] + letterGuess + pordle[i+1:]

        print("Used letters: ")
        print(lettersUsed)
        print(" ".join(pordle)) #Print the string with guessed letters with spaces in between
        numGuesses += 1

    print("Well done! You guessed in " + str(numGuesses-1) + " guesses!")

main()
