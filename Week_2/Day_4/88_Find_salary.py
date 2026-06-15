# Find salary.

salary = int(input("Enter salary in digits: "))

if salary < 1:
    print("Invalid salary")

elif salary < 20000:
    print("You belong to lower-class.")

elif salary < 40000:
    print("You belong to lower-middle-class.")

elif salary < 60000:
    print("You belong to middle-class.")

elif salary < 90000:
    print("You belong to upper-middle-class.")

elif salary < 120000:
    print("You belong to alead-class.")

else:
    print("You are very rich.")