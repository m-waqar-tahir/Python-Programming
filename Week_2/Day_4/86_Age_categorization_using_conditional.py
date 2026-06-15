# Age categorization using conditionals.

age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")

elif age > 120:
    print("Invalid age")

elif age < 18:
    print("You are a kid.")

elif age < 30:
    print("You are an adult.")

elif age < 50:
    print("You are a youngster.")

elif age < 70:
    print("You are a senior citizen.")

elif age < 100:
    print("You are an older person.")

else:
    print("You are very old.")