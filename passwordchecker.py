import string
work = True
while work:
    password = input("Enter your password:")

    if len(password) > 11 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and any(i in string.punctuation for i in password):
        print("Password is strong.")
        work = False
    elif any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password):
        print("Password is ok.")
        work = False
    else:
        print("Password is too weak. Make it stronger.\nThere should be more characters, numbers and characters of punctuation.")

