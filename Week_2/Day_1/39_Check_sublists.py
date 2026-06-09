# Check if a list contains sublist or sublists
list1 = [1, 2, 3, 4, 5]
sublist1 = [2, 3]
sublist2 = [4, 5]

print(sublist1 in list1)  # Output: False
print(sublist2 in list1)  # Output: False

# Check if a list contains all elements of a sublist
print(all(item in list1 for item in sublist1))  # Output: True
print(all(item in list1 for item in sublist2))  # Output: True