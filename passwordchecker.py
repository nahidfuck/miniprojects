import string

def check_password(userpassword):
    if len(userpassword) < 8:
        print("Password is weak, try to add more characters")
    elif any(char.isupper() for char in userpassword) and any(char.islower() for char in userpassword) and any(char.isdigit() for char in userpassword):
        print("Password is ok, but you can add punctuation characters")
    elif any(char.isupper() for char in userpassword) and any(char.islower() for char in userpassword) and any(string.punctuation) in userpassword:
        print("Password is strong, good")

check_password(input("Enter your password:\n"))
