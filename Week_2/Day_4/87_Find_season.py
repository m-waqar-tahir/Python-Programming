# Finding season by month number.

month = int(input("Enter month number: "))

if month < 1:
    print("Invalid month")

elif month > 12:
    print("Invalid month")

elif month < 3:
    print("Winter")

elif month < 6:
    print("Spring")

elif month < 9:
    print("Summer")

elif month < 12:
    print("Autumn")

else:
    print("Winter")