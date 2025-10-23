import random

words = ["python", "keyboard", "laptop"]
work = True

print("Welcome to the Hangman game!")
gamemode = input("Choose your gamemode (write 1 or 2):\n1. Come up with a word yourself\n2. The computer will give you a word\n")
if gamemode == "1":
    guessword = input("Your word for Hangman:\n")
elif gamemode == "2":
    guessword = random.choice(words)
else:
    print("You can enter only 1 or 2")

guessedword = ["_"] * len(guessword)

print("Let's start, your word is ready!" \
"For now you have only 6 attempts.")

while work:
    print(f"Your word: {" ".join(guessedword)}:")
    yourletter = input("Letter: ")
    for i in range(len(guessword)):
        if guessword[i] == yourletter:
            guessedword[i] = yourletter
            print("Nice one, let's go")
        else:
            print("Nope, try again")
