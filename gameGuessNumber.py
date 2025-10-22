import random

work = True
guessnum = random.randrange(1, 101)

while work:
    a = int(input("Вгадай число від 1 до 100: "))
    if a == guessnum:
        print("Legend, koniec zabawy")
        work = False
    elif a > guessnum:
        print("Bzdura, mniej")
    elif a < guessnum:
        print("Bzdura, wiecej")