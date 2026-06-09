# Check common members in two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_members = list(set(list1) & set(list2))
print(common_members)  # Output: [4, 5]