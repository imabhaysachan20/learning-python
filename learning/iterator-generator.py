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

class MyRange:
    def __init__(self,start,end):
        self.value = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value>=self.end:
            raise StopIteration
        current = self.value
        self.value+=1
        return current  

num = MyRange(1,10)

print(next(num))

# for n in num:
#     print(n)

#generators
