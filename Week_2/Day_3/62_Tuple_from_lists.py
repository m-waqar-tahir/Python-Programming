# It does not change the inner items, but only the outer type of the variable.
list1 = [[1, 2, 3, "I", 'am', 'learning', 'python.'], [23, 34, 5.5]]

tuple1 = tuple(list1)

print("The newly created variable is of type: ", type(tuple1))
print(tuple1)

# Output
# The newly created variable is of type: <class 'tuple'>
# ([1, 2, 3, 'I', 'am', 'learning', 'python.'], [23, 34, 5.5]) 