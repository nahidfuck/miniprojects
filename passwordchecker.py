import string
work = True
while work:
    password = input("Napisz swoje hasło:")

    if len(password) > 11 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and any(i in string.punctuation for i in password):
        print("Hasło jest mocne.")
        work = False
    elif any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password):
        print("Hasło jest śriednie.")
        work = False
    else:
        print("Hasło jest za słabe. Wprowadź silniejsze hasło.\nMusi być co najmniej 8 znaków, cyfr oraz wielkie i małe litery.")

