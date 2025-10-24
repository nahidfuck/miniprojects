import random

words = [
    "python", "keyboard", "laptop",
    "monitor", "computer", "programmer", "internet", "browser", "network", "software",
    "hardware", "database", "function", "variable", "compiler", "terminal", "debugger",
    "algorithm", "password", "storage", "cloud", "server", "desktop", "notebook",
    "headphones", "microphone", "display", "router", "screen", "memory", "cursor",
    "binary", "command", "project", "backend", "frontend", "developer", "machine",
    "virtual", "syntax", "execute", "integer", "boolean"
]

work = True
attempts = 6

print("Welcome to the Hangman game!")
gamemode = input("Choose your gamemode (write 1 or 2):\n1. Come up with a word yourself\n2. The computer will give you a word\n")
if gamemode == "1":
    guessword = input("Your word for Hangman:\n")
elif gamemode == "2":
    guessword = random.choice(words)
else:
    print("You can enter only 1 or 2")

guessedword = ["_"] * len(guessword)

print("Let's start, your word is ready!\nFor now you have only 6 attempts.")

while attempts > 0 and "_" in guessedword:
    print(f"Your word: {" ".join(guessedword)}:")
    yourletter = input("Letter: ")
    if yourletter in guessword:
        for i in range(len(guessword)):
            if guessword[i] == yourletter:
                guessedword[i] = yourletter
        print("Nice one, let's go")
    else:
        attempts -= 1
        print(f"Nope, try again, you have {attempts} attempts left")

print("\nGame over!")
if "_" not in guessedword:
    print(f"You won! The word was '{guessword}'.")
else:
    print(f"You lost. The word was '{guessword}'.")