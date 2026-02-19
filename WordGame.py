#Word Game is a knock-off version of a popular online word-guessing game.
#WordGame.py
#Name: Riley Mayfield
#Date:  1/18
#Assignment: Lab 5
#Purpose: Create deeper understanding of what you can do with strings

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    return letter in word


def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""

    return word[spot] == letter

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""

    result = ""

    for ch in range(len(myGuess)):
        if inSpot(myGuess[ch], word, ch):
            result += myGuess[ch].upper()
        elif inWord(myGuess[ch], word):
            result += myGuess[ch].lower()
        else:
            result += "*"
    return result


def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    tries = 6
    print(todayWord)

    print("Let's play a Game")
    #User should get 6 guesses to guess

    while tries > 0:
        guess = input(f"You have {tries} guesses\nEnter a 5 letter word: ")
        while 5 != len(guess):
            print("Invalid word length, try again")
            guess = input(f"You have {tries} guesses\nEnter a 5 letter word: ")
        guess = guess.lower()
        feedback = rateGuess(guess, todayWord)
        print("Result", feedback)

        if guess == todayWord:
            print(f"You guessed correctly with {tries-1} guesses left!")
            return
        
        tries = tries - 1
        
    print(f"Sorry the word was {todayWord}")
    #Ask user for their guess
    #Give feedback using on their word:





if __name__ == '__main__':
  main()
