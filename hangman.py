#! /usr/bin/env python3

from ANSI import *
import random

def GetWord():
    words = []
    file = open("words.txt","r")
    for line in file.readlines():
        words.append(line.rstrip('\n'))
    return words[random.randint(0,len(words)-1)]

word = GetWord() 
current = ("_ ," * len(word)).split(',')
letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

def Compare(word, current, guess):
    if len(guess) > 1:
        if guess == word:
            Win()
        else:
            Lose()

    for i in range(len(letters)):
        if letters[i] == guess:
            letters[i] = f"{BG.RED}{letters[i]}"

    for i in range(len(word)):
        if word[i] == guess:
           current[i] = f"{guess} "
        
def WordList():
    for i in range (len(letters)):
        print(f"{BG.GREEN}{letters[i]}",end=" " if (i+1) % 13 else "\n")
    print(UTIL.RESET)

def Hangman(guess):
    for i in range(len(guess)):
        print(guess[i],end="")
    print("")

def Win():
    print(f"{FG.GREEN}{UTIL.BOLD}Good job, you win :){UTIL.RESET}")
    exit()

def Lose():
    print(f"{FG.RED}{UTIL.BOLD}Too bad, you lose :({UTIL.RESET}")
    print(f"Your word would have been: {UTIL.UNDERLINE}{word}{UTIL.RESET}")
    exit()

def CheckState(current,guesses_left):
    if guesses_left == 0:
        Lose()

    for i in range(len(current)):
        if current[i] == "_ ":
            return
    Win()

def Render(current,guesses_left):
    print(UTIL.CLEAR + UTIL.TOP,end="")
    print(f"{UTIL.BOLD}Hangman by PsychicPenguin{UTIL.RESET}\n")
    WordList()
    Hangman(current)

def Update(word,current,guesses_left):
    CheckState(current,guesses_left)
    Compare(word,current,input(f"Guess a letter [{guesses_left}]: "))

if __name__ == "__main__":
    try:
        guesses = len(word)*2
        for i in range(guesses+1):
            Render(current,guesses-i)
            Update(word,current,guesses-i)
    except KeyboardInterrupt:
        exit(0)
