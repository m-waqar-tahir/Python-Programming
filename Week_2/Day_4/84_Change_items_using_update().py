# Changing dictionary items using update() method.

profile = {"name": "Waqar", "surname": "Tahir", "birthday_year": 2000}
profile.update({"birthday_year": 2001}) # value changed through it's key.

print(profile)

# Output:
# {'name': 'Waqar', 'surname': 'Tahir', 'birthday_year': 2001}