# Select random items from a list without importing the random module

list_of_items = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# Get the length of the list
list_length = len(list_of_items)

print(list_of_items[5 % list_length])  # This will select a random item based on the index