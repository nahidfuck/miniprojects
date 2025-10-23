import random

work = True
guessnum = random.randrange(1, 101)

while work:
    a = int(input("Guess number from 1 to 100: "))
    if a == guessnum:
        print("Legend, koniec zabawy")
        work = False
    elif a > guessnum:
        print("Bzdura, less")
    elif a < guessnum:
        print("Bzdura, more")