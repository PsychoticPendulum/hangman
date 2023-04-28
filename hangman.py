#! /usr/bin/env python3

from ANSI import *
import random
import sys

def GetWord():
    if len(sys.argv) > 1:
        return sys.argv[1].lower()
    words = []
    try:
        file = open("words.txt","r")
        for line in file.readlines():
            words.append(line.rstrip('\n'))
    except PermissionError:
        print("ERROR: Insufficient permissions to read wordlist")
        exit(1)
    except FileNotFoundError:
        print("ERROR: Unable to locate wordlist")
        exit(1)
    except:
        print("ERROR: Unknown error")
        exit(1)
        
    return words[random.randint(0,len(words)-1)]

class Stats:
    word = GetWord() 
    current = ("_ ," * len(word)).split(',')
    fails = 0

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

gallows = [
    "        \n"
    "        \n"
    "        \n"
    "        \n"
    "        \n"    
    "        \n"    
    "--------\n",

    "|       \n"
    "|       \n"
    "|       \n"
    "|       \n"
    "|       \n"    
    "|       \n"    
    "+-------\n",

    "+----+  \n"
    "|       \n"
    "|       \n"
    "|       \n"
    "|       \n"    
    "|       \n"    
    "+-------\n",

    "+----+  \n"
    "|    |  \n"
    "|       \n"
    "|       \n"
    "|       \n"    
    "|       \n"    
    "+-------\n",

    "+----+  \n"
    "|    |  \n"
    "|    o  \n"
    "|       \n"
    "|       \n"    
    "|       \n"    
    "+-------\n",

    "+----+  \n"
    "|    |  \n"
    "|    o  \n"
    "|    T  \n"
    "|       \n"    
    "|       \n"    
    "+-------\n",

    "+----+  \n"
    "|    |  \n"
    "|    o  \n"
    "|   /T  \n"
    "|       \n"    
    "|       \n"    
    "+-------\n",

    "+----+  \n"
    "|    |  \n"
    "|    o  \n"
    "|   /T\ \n"
    "|       \n"    
    "|       \n"    
    "+-------\n",

    "+----+  \n"
    "|    |  \n"
    "|    o  \n"
    "|   /T\ \n"
    "|   /   \n"    
    "|       \n"    
    "+-------\n",

    "+----+  \n"
    "|    |  \n"
    "|    o  \n"
    "|   /T\ \n"
    "|   / \ \n"    
    "|       \n"    
    "+-------\n",
]

def Compare(word, current, guess):
    if len(guess) > 1:
        if guess == word:
            Win()
        else:
            Lose()

    for i in range(len(letters)):
        if letters[i] == guess:
            letters[i] = f"{BG.RED}{letters[i]}"

    hit = False
    for i in range(len(word)):
        if word[i] == guess:
           hit = True
           current[i] = f"{guess} "

    if hit == False:
        Stats.fails += 1
        
def WordList():
    for i in range (len(letters)):
        print(f"{BG.GREEN}{FG.BLACK}{letters[i]}",end=" " if (i+1) % 13 else "\n")
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
    print(f"Your word would have been: {UTIL.UNDERLINE}{Stats.word}{UTIL.RESET}")
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
    print(gallows[Stats.fails])
    Hangman(current)

def Update(word,current,guesses_left):
    CheckState(current,guesses_left)
    Compare(word,current,input(f"Guess a letter [{guesses_left}]: ").lower())

if __name__ == "__main__":
    guesses = len(gallows)-1
    try:
        while True:
            Render(Stats.current,guesses-Stats.fails)
            Update(Stats.word,Stats.current,guesses-Stats.fails)
    except KeyboardInterrupt:
        exit(0)
