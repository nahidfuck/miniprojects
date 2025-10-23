import math

print("ax^2+bx+c=0\n")
a = float(input("Enter value а: "))
b = float(input("Enter value b: "))
c = float(input("Enter value c: "))
d = b**2-4*a*c

if a == 0:
    x = -c / b
    print(f"\n{int(a)}x^2+{int(b)}x+{int(c)}=0")
    print("\nAnswer:", x)
else:
    if d > 0:
        x1 = (-b - math.sqrt(d))/2*a
        x2 = (-b + math.sqrt(d))/2*a
        print(f"\n{int(a)}x^2+{int(b)}x+{int(c)}=0")
        print("\nAnswer:")
        print("x1 =", round(x1, 3))
        print("x2 =", round(x2, 3))
    else:
        if d == 0:
            x = -b/2*a
            print(f"\n{int(a)}x^2+{int(b)}x+{int(c)}=0")
            print("\nAnswer:", x)
        else:
            print("\nKoniec zabawy")