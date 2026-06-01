'''
Identity operator

Return's True, if both variables are the same objects (memory address)

'''

x = ['hello', 'world']
y = [1,2,3,4]
z = x
x.append('hi')
print(z)
print(id(x))
print(id(z))
print(x)
if z is x:
    print('Return\'s True, if both variables are the same objects')
    
else:
    print('It\'s not a Identity operator')

x = ["python", "git", "aws"]
print(id(x))
y = ["python", "git", "aws"]
print(id(y))
print(x is y) # False because values are same but not the objects


x = (1,2,3)
y = x
print(x is y)


x = 4
y = 5
print(x is y)

#pooling

x = 5
y = 5

print(x==y)



# # Addition 
# a = 20
# b = 25
# print(a+b)

# # Example 2
# x = 20
# y = x+20
# print(y)

# # Subtraction 
# y = 165
# z = 65
# print(y-z)

# # Subtraction using function
# def subtraction(a, b):
#     return a-b
    
# x = subtraction(165, 65)
# print(x)

# #Multiplication
# x = 10
# y = 20
# z = x*y
# print(f'the multiplication of {x} and {y} is:- {z}'.format(x, y, z))

# # Division
# x = 10
# y = 2
# print(x/y)

# #Modulus 
# x = 20
# y = 10
# print(x % y)

# #Exponentiation 
# z = 2
# y = 5
# print(2 ** 5)

# # //Floor Division
# x = 10//2
# print(x)

# # 2)Assignment Operators
# x = 2
# print(x)

# x = 2
# x = x+3 # x=x+3 is same as  x+=3
# print(x)

# x = 3
# x = x-1 # x=x-1 is same as x-=1
# print(x)

# x = 3
# x = x*3 # x=x*3 is same as x*=3
# print(x)

# x = 10
# x = x/3 # x=x/3 is same as x/=3
# print(x)

# x = 10
# x = x%2 # x=x%2 is same as x%=2
# print(x)

# x = 10
# x = x//2 # x=x//2 is same as x//=3
# print(x)

# x = 10
# x = x**5 # x=x**2 is also same as x**=2
# print(x)

# # example for augmented assignment operator 

# text = 'hello world '
# text += 'python'
# print(text)

# # Comparision operators
# x = 10
# y = 10
# if(x == y): # equal to(==) operator checks both number's are equal or not 
# 	print("yes, both are equal")
# else:
# 	print("no, both are not equal")


# #Not equal to(!=)
# a = 20
# b = 40
# if  a != b:
# 	print("yes")
# else:
# 	print("no")

# #Greater than or not (>)
# a = 20
# b = 40
# if  a>b:
# 	print("yes")
# else:
# 	print("no")

# #Less than (<)
# a = 20
# b = 40
# if  a<b:
# 	print("yes")
# else:
# 	print("no")

# #Greater than or equal to(>=)
# a = 20
# b = 40
# if  a>=b:
# 	print("yes")
# else:
# 	print("no")

# #Less than or equal to(<=)
# a = 20
# b = 40
# if  a<=b:
# 	print("yes")
# else:
# 	print("no")
	
# # identity operators are used to check both variable objects are same or not 
# # is 

# z = x
# print(z is x) # Returns True because both objects are same z and x.
# print(x is z) # True 

# # is not return True if both variable objects are not same 
# x = ["python", "git", "aws"]
# y = ["python", "git", "aws"]
# z = x
# print(z is not x) # Returns False because both variable objects are same 
# print(x is not y) # Returns True because both variables are diff objects 

# '''
# 1)and - Returns True if both statements are True
# 2)or - Return True if any one statement is True
# 3)not - Return True, if statement is False, it opposite's the answer.
# '''
# # and 
# val = 10
# val1 = 20
# val2 = 30
# if (val < val1) and (val2 > val1): # both statements are True 
#   print("Both statements are True")
# else:
#   print("Both statements are False")
  
# # or
# val = 10
# val1 = 20
# val2 = 30
# if (val > val1) or (val2 > val1): # here one statement is False and other one is True 
#   print("Both statements are True")
# else:
#   print("Both statements are False")
  
# # not
# val = 10
# val1 = 20
# val2 = 30
# if (not(val < val1) and (val2 > val1)): # both statements are True 
#   print("Both statements are True")
# else:
#   print("Both statements are False")

# '''
# Membership operators are used to check certain sequence is present in the object
# are not  
# '''
# x = ["Docker", "Azure", "Linux"]
# print("Linux" in x)

# '''
# not in membership operator returns True if the specified value is not present in
# the object 
# '''
# x = ["Docker", "Azure", "Linux"]
# print("Linux" not in x) # False 

# '''
# Membeship operator:-

# Returns True, if a sequence with the specified value present in the object.

# '''


# x = ['hello', 'world']
# if 'hello' in x:
#     print("Returns True, if a sequence with a specified value present in the object.")
# else:
#     print('It\'s not a Membership operator')
	

# '''
# (), **, *, /, +, - it means which operator will execute first. 
# ''' 
# print((5 + 4) * 10 / 2) 
# # 45.0

# print(((5 + 4) * 10) / 2)
# # 45.0

# print((5 + 4) * (10 / 2))
# # 45.0

# print(5 + (4 * 10) / 2)
# #25.0

# print(5 + 4 * 10 // 2)
# # 25