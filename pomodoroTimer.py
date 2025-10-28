import time

mode = input("Enter your timer timer mode:\n1. Pomodoro (25 minutes)\n2. Input time by yourself\n")
if mode == '1':
    s = 0
    m = 25

    while m > 0 and s >= 0:
        print(f"{m:02}:{s:02}", end="\r")
        time.sleep(1)
        s -= 1
        if s < 0:
            m -= 1
            s = 59

    print("00:00\nTime's up! Take a break.")

elif mode == '2':
    h = int(input("Enter hours: "))
    m = int(input("Enter minutes: "))
    s = int(input("Enter seconds: "))

    if h <= 0 or m <= 0 or s <= 0 or m >= 60 or s >= 60:
        print("Invalid input. Please enter positive values for hours, minutes (0-59), and seconds (0-59).")
        exit()
    while h >= 0 and (m >= 0 or h > 0) and (s >= 0 or m > 0 or h > 0):
        print(f"{h:02}:{m:02}:{s:02}", end="\r")
        time.sleep(1)
        s -= 1
        if s < 0:
            m -= 1
            s = 59
        if m < 0:
            h -= 1
            m = 59

    print("00:00:00\nTime's up! Take a break.")