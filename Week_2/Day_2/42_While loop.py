# While loop in list

list1 = [1, 2, 3]
list2 = ['I', 'am', 'learning', 'Python.']

i = 0
x = 0
while i < len(list1) | x < len(list2):
    print(list1[i], list2[x])
    i = i + 1
    x = x + 1


# Output:
# 1 I
# 2 am
# 3 learning
# This is a tricky exercise.
# You have to find out how to solve this problem of 1 last item of list 2 not printing.