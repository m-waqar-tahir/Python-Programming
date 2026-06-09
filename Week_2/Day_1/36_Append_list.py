# Append item to a list
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Append another list to the existing list
another_list = [5, 6]
my_list.extend(another_list)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Append a string to the list
my_list.append("Hello")
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 'Hello']

# Append a tuple to the list
my_tuple = (7, 8)
my_list.extend(my_tuple)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 'Hello', 7, 8]

# Append a dictionary to the list
my_dict = {'key1': 'value1', 'key2': 'value2'}
my_list.extend(my_dict.items())
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 'Hello', 7, 8, ('key1', 'value1'), ('key2', 'value2')]