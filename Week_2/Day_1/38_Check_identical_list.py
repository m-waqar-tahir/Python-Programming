# Check if two lists are identical
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
list3 = [5, 4, 3, 2, 1]

print(list1 == list2)  # Output: True
print(list1 == list3)  # Output: False

# Check if two lists are identical regardless of order
print(set(list1) == set(list3))  # Output: True