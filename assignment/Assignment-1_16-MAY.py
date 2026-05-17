# list creation 
l = [1, 33, 56, 1001, 768]

#adding 89 to the end of list using append() method
l.append(89)
print(l) 

#adding 39 to the beginnnig of the list 
l.insert(0,39)
print(l)

#adding another list into the existing list
l.extend([77,66,44])
print(l)

#adding another list inside a list in nested manner
l.append([99,88])
print(l)

#adding apple at 2nd position
l.insert(1,'apple')
print(l)

#finding apple and replacing it with pineapple
if "apple" in l:
    l[l.index("apple")] = "pineapple"
print(l)

#removing element at position 4
l.pop(3)
print(l)

#removing pineapple first occurence
l.remove('pineapple')
print(l)