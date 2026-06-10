nums = [1,2,3]

# for num in nums:
#     print(num)

# print(dir(nums))

# print(nums.__iter__())

# print(next(nums)) #error since list is an iterable not iterator

# #iterable is any class instance in python which implements __iter__ method!

# i_nums = nums.__iter__()


# print(i_nums)
# print(dir(i_nums))

# # next function calls the __next__ method 
# # iter function calls the __iter__ method 
# # any object that has __next__ method implemented is an iterator
 

# i_nums = iter(nums)

# print(i_nums)
# # print(dir(i_nums))

# #iterators are also iterable so they also have __iter__ method implemented
# #__iter__ of an iterator just returns itself (self)

# print(next(i_nums))


# #iterator is an object with state so it remeber where it is 

# print(next(i_nums))
# print(next(i_nums))

# print(next(i_nums)) # throws StopIteration Exception when runs out of elements

# ##for loop internal working
# #calls __iter__ method of any iterable and get the iterator and calls next function until it gets StopIterationException

# #internal working of for loop

# nums = [1,2,3,4]

# nums_itr = nums.__iter__()
# while True:
#     try:
#         print(next(nums_itr))
#     except StopIteration:
#         break

##we can make our own iterator object!

# class MyRange:
#     def __init__(self,start,end):
#         self.value = start
#         self.end = end
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.value>=self.end:
#             raise StopIteration
#         current = self.value
#         self.value+=1
#         return current  

# num = MyRange(1,10)

# print(next(num))

# for n in num:
#     print(n)

#generators
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result

my_nums = square_numbers([1, 2, 3, 4, 5])
# my_nums = [x*x for x in [1,2,3,4,5]]

print (my_nums)  # [1, 4, 9, 16, 25]

# for num in my_nums:
#     print num
def square_numbers(nums):
    for i in nums:
        yield (i * i)
    
my_nums = square_numbers([1, 2, 3, 4, 5])
# my_nums = [x*x for x in [1,2,3,4,5]]

print (my_nums)  # generator object
print (next(my_nums))

#advantage

my_nums = [x**x for x in range(0,100)]
##100 elements in memory!!

my_nums = (x**x for x in range(0,100))
## just an generator object which will give us simply when we ask next thing

print(my_nums)
next(my_nums)

# can be converted to list using list()

my_nums_list = list(my_nums)

import random
import time
names = ["Alice", "Bob", "Charlie", "Diana"]
majors = ["Computer Science", "Mathematics", "Physics", "Biology"]
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person 

t1 = time.perf_counter()

people = people_list(1000000)
t2 = time.perf_counter()

print("time taken list", t2-t1)

t1 = time.perf_counter()

people = people_generator(1000000)
t2 = time.perf_counter()

print("time taken generator", t2-t1)


##generator used to make iterator

def make_range(start,end):
    current = start
    while current<end:
        yield current
        current+=1

num = make_range(1,10)
print(next(num))