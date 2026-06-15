# Printing Military Time Format using conditionals

h = int(input("Hour: "))
m = int(input("Minute: "))
s = int(input("Second: "))

if h < 0:
    print("Invalid hour")

elif h > 23:
    print("Invalid hour")

elif m < 0:
    print("Invalid minute")

elif m > 59:
    print("Invalid minute")

elif s < 0:
    print("Invalid second")

elif s > 59:
    print("Invalid second")

else:
    print(h, ":", m, ":", s)