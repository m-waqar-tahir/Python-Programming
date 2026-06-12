# Tuple items updation

x = ("apple", "banana", "cherry") # The existing tuple.

print("The existing tuple is: ", x) 

y = list(x)       # Here the typle x is converted into a list using list() constructor.
print("After converting to list, it shows as: ", y)

y[1] = "kiwi"     # Here the item of that list is accessed using y[1], which is "banana", and a new item is assigned to that index as "kiwi".
print("After making the required changes into that list: ", y)

x = tuple(y)      # Here after making the required changes, the list is again converted into the tuple using tuple() constructor.
print("The list is again converted into a typle shown as: ", type(x))

# Output:
# We can verify by checking the type of the same variable before and after making changes.

# The existing tuple is:  ('apple', 'banana', 'cherry')
# After converting to list, it shows as:  ['apple', 'banana', 'cherry']
# After making the required changes into that list:  ['apple', 'kiwi', 'cherry']
# The list is again converted into a typle shown as:  <class 'tuple'>