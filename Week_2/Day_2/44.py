# Creating an empty list and filled with the items of an existing list.

list1 = ["My", "name", "is", "Waqar", "Tahir."]
list2 = []

for x in list1:
    list2.append(x)

print("New generated list is: ", list2)

# Output:
# New generated list is: ['My', 'name', 'is', 'Waqar', 'Tahir.']