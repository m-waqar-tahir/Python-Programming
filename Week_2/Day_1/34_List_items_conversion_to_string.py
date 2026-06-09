# List items conversion to string
my_list = [1, 2, 3, 4, 5]
string_list = [str(i) for i in my_list]
print(string_list)  # Output: ['1', '2', '3', '4', '5']
# Alternatively, into single string
single_string = ''.join(string_list)
print(single_string)  # Output: 1, 2, 3, 4, 5