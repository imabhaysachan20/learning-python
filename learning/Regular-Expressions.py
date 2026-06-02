import re

text_to_search = r'''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

abhay.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

cat is in the category of cat that are not lion using the concatenation of special catc
abc

Mr. Kohli
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

#raw string ignores escape character

# print('\tTab') #normal
# print(r'\tTab') #raw string

# pattern  = re.compile(r'abc')

# matches = pattern.findall(text_to_search)
# matches2 = pattern.finditer(text_to_search)

# print(matches)
# print(matches2)

# for x in matches2:
#     print(x)

# print(text_to_search[1:4],text_to_search[221:224])


#case sensitive 
#ordered

#seaching for .
# pattern2 = re.compile('.')
# match3 = pattern2.findall(text_to_search)

# for x in match3:
#     print(x) #gives everything as . is special regex character



# pattern3 = re.compile(r'\.')

# for x in pattern3.finditer(text_to_search):
#     print(x)


# pattern4 = re.compile(r'abhay.com')

# for x in pattern4.finditer(text_to_search):
#     print(x)

# Patterns

# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)

# patter4 = re.compile(r'\d')

# for x in patter4.finditer(text_to_search):
#     print(x)

# patter5 = re.compile(r'\D')

# for x in patter5.finditer(text_to_search):
#     print(x)

# pattern6 = re.compile(r'\w')

# for x in pattern6.finditer(text_to_search):
#     print(x)

# pattern7 = re.compile(r'\s')

# for x in pattern7.finditer(text_to_search):
#     print(x)


# Anchors
# \b      - Word Boundary
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String

# patter8 = re.compile(r'\bcat\b')

# for x in patter8.finditer(text_to_search):
#     print(x)

# patter9 = re.compile(r'\Bcat')

# for x in patter9.finditer(text_to_search):
#     print(x)

