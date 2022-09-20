# LISTS
# Create a list option 1:
# l = []
# print(l)

# Create a list option 2:
# l = [1, 'string', 12.3, 'Hello', 25]
# print(l)

# Create a list option 3:
# sentence = 'What a wonderful life?'
# my_list = list(sentence)
# print(my_list)
# function list divided the whole sentence in letters

# Create a list option 3-1:
# sentence = 'What a wonderful life?'
# my_list = sentence.split(' ')
# print(my_list)
# function split divided the whole sentence with ' '

# Create a list option 3-2:
# sentence = 'What a wonderful life?'
# my_list = sentence.split(' ')
# print(my_list[-1])
# print(my_list[0])
# function print index #


# For loop is with list
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
# print(num*2)
# will print a list with [2, 4, 6, 8, 10]

# In-place list mutating

# l = [8, 7, 5, 10]
# print(l)
# print(id(l))

# l1 = [25, 80]
# l.append(l1)
# print(l)
# print(id(l))

# add = 'extra'
# l.append(add)
# l1.extend(add)
# print(l)
# print(l1)

# .sort() and sorted()
#
# nums = [2, 3, 1, 5, 6, 4, 0]
# print(f'Initial list: {nums}')
# print(id(nums))

# print('SORTED()')
# print(f'New sorted list: {sorted(nums)}')
# printed in order

# print(id(sorted(nums)))
# print('.SORT()')
# print(nums.reverse())
# print(nums)
# print(id(nums))

# slicing
# letters = ['a', 'b', 'c', 'd', 'e', 'f']
# print(letters[0:-1:2])
# ['a', 'c', 'e']
# print(letters[-3])
# d
# print(letters[::-1])
# ['f', 'e', 'd', 'c', 'b', 'a']
# print(letters[1:-1])
# ['b', 'c', 'd', 'e']

# List comprehension

# li = [1, 2, 3, 4, 5]
# new_li = []
# for x in li:
#     if x%2:

#         new_li.append(x*x)
#         print(new_li)

# l = [1, 2, 3, 4, 5]
# new_l = [x*x for x in l if x%2==0]
# print(new_l)

# my_tuple = 1, 2, 3
# print(my_tuple)

# name = ('Mark',)
# print(name)

#letters = ('apple', 'banana', 'cat')
# a, b, c = letters
# print(a)
# print(b)
# print(c)


# letters = ('apple', 'banana', 'cat')
# letters = list(letters)
# letters[0] = 'ananas'
# print(letters)

# my_tuple = (1, True, 'name', None, 'name', 25)
# result = tuple(filter(lambda x: isinstance(x, int), my_tuple))
# filter integer class
# print(result)

# result = tuple(filter(lambda x: isinstance(x, str), my_tuple))
# filter string class
# print(result)

# print(f'Sum is: {sum(result)}')
# print(f'Max is: {max(result)}')
# print(f'Min is: {min(result)}')

# for(index, item) in enumerate(my_tuple):
#    print(index, item)
# assign index for each element

# nested list in tuple
# letters = ('apple', ['ananas', 'mango'], 'melon')
# letters[1][1] = 'cherry'
# print(letters)
# answer: ('apple', ['ananas', 'cherry'], 'melon')

# passing tuple as an argument in function
# def sum_it(*args):
#    total = 0
#    for num in args:
#        total += num
#    return total
# print(sum_it(4, 5, 10, 6, 20, 100))
# returns sum of numbers

# def func(*args):
#     l = []
#     for item in args:
#         l.append(item*item)
#    return l
# print(func(2, 5, 6, 8, 10))

# dictionary

my_dict = {
    'name': 'Anna',
    'last_name': 'Pavlov',
    'age': 35,
    'department': 'IT'
}
print(my_dict)
print(id(my_dict))
print(my_dict['name'])
print(len(my_dict))
print(len(my_dict.keys()))

my_dict['salary'] = 5000
print(len(my_dict.keys()))
print(my_dict.values())
print(my_dict.pop('salary'))
print(my_dict)

# sets

#print(set([1, 2, 3, 3, 10, 3, 4]))

set1 = {1, 2, 3, 'one', 'ten'}
set2 = {1, 2, 3, 'one', 'ten', 100, 525}
set3 = {1, 2, 3}

print(set1.issuperset(set2))
print(set2.issuperset(set1))
print(set2.difference(set1))

fs = frozenset({1, 2, 3})
print(fs)
fs.remove(1)
print(fs)

fs.add(4)
print(fs)

l = [8, 7, 5, 10, 'j', 'string']
l1 = [1, 2]
print(l + l1)
