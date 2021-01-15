# Q1.1

def myreduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value


# Q1.2

def myfilter(function, iterable):
    list_result=[]
    for element in iterable:
        if function(element) == True:
            list_result.append(element)
    return list_result



# Q2.

# l1 = ['x', 'y', 'z']

# output = []

# for i in l1:
#     strx=''
#     for i in range(0,4):
#         strx += j
#	  output.append(strx)

# range(0, len(l1))
# print(output)


my_list1 = [(letters * alphabets) for letters in 'xyz' for alphabets in range(1, 5)]
print(my_list1)


my_list2 = [(letters * alphabets) for alphabets in range(1, 5) for letters in ['x', 'y', 'z'] ]
print(my_list2)

my_list3 = [[i + j] for j in [0, 1, 2] for i in range(2, 5)]
print(my_list3)


my_list4 = [[i + j for j in [0, 1, 2, 3]] for i in range(2, 6)]
print(my_list4)

my_list6 = my_list3 + my_list4
print(my_list6)


my_list5 = [(i,j) for j in [1, 2, 3] for i in [1, 2, 3]]
print(my_list5)

