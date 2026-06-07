import re

# text_to_search = r'''
# abcdefghijklmnopqurtuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1234567890

# Ha HaHa

# MetaCharacters (Need to be escaped):
# . ^ $ * + ? { } [ ] \ | ( )

# abhay.com

# 321-555-4321
# 123.555.1234
# 123*555*1234
# 123--555--1234
# 800-555-1234
# 900-555-1234

# cat is in the category of cat that are not lion using the concatenation of special catc
# abc

# Mr. Kohli
# Mr Smith
# Ms Davis
# Mrs. Robinson
# Mr. T
#fff
# cat
# bat
# rat
# lat
# '''

# sentence = 'Start a sentence and then bring it to an end'

# #raw string ignores escape character

# # print('\tTab') #normal
# # print(r'\tTab') #raw string

# # pattern  = re.compile(r'abc')

# # matches = pattern.findall(text_to_search)
# # matches2 = pattern.finditer(text_to_search)

# # print(matches)
# # print(matches2)

# # for x in matches2:
# #     print(x)

# # print(text_to_search[1:4],text_to_search[221:224])


# #case sensitive 
# #ordered

# #seaching for .
# # pattern2 = re.compile('.')
# # match3 = pattern2.findall(text_to_search)

# # for x in match3:
# #     print(x) #gives everything as . is special regex character



# # pattern3 = re.compile(r'\.')

# # for x in pattern3.finditer(text_to_search):
# #     print(x)


# # pattern4 = re.compile(r'abhay.com')

# # for x in pattern4.finditer(text_to_search):
# #     print(x)

# # Patterns

# # .       - Any Character Except New Line
# # \d      - Digit (0-9)
# # \D      - Not a Digit (0-9)
# # \w      - Word Character (a-z, A-Z, 0-9, _)
# # \W      - Not a Word Character
# # \s      - Whitespace (space, tab, newline)
# # \S      - Not Whitespace (space, tab, newline)

# # patter4 = re.compile(r'\d')

# # for x in patter4.finditer(text_to_search):
# #     print(x)

# # patter5 = re.compile(r'\D')

# # for x in patter5.finditer(text_to_search):
# #     print(x)

# # pattern6 = re.compile(r'\w')

# # for x in pattern6.finditer(text_to_search):
# #     print(x)

# # pattern7 = re.compile(r'\s')

# # for x in pattern7.finditer(text_to_search):
# #     print(x)


# Anchors
# # \b      - Word Boundary
# # \B      - Not a Word Boundary
# # ^       - Beginning of a String
# # $       - End of a String

# # patter8 = re.compile(r'\bcat\b')

# # for x in patter8.finditer(text_to_search):
# #     print(x)

# # patter9 = re.compile(r'\Bcat')

# # for x in patter9.finditer(text_to_search):
# #     print(x)

# sentence = "hey there welcome to this regular expression tut"

# # pattern10 = re.compile(r'^hey')

# # for x in pattern10.finditer(sentence):
# #     print(x)

# # pattern11 = re.compile(r'^ther')

# # for x in pattern11.finditer(sentence):
# #     print(x) 

# # pattern12 = re.compile(r'tut$')

# # for x in pattern12.finditer(sentence):
# #     print(x)

# # pattern12 = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# # for x in pattern12.finditer(text_to_search):
# #     print(x)



# # []      - Matches Characters in brackets single character
# # [^ ]    - Matches Characters NOT in brackets
# # |       - Either Or
# # ( )     - Group


# # pattern13 = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

# # for x in pattern13.finditer(text_to_search):
# #     print(x)

# # pattern14 = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
# # for x in pattern14.finditer(text_to_search):
# #     print(x)

# # '-' inside [] if in start is normal - otherwise in between it is range 0-5

# # pattern14 = re.compile(r'[0-2]')
# # for x in pattern14.finditer(text_to_search):
# #     print(x)

# # pattern14 = re.compile(r'[a-zA-Z]')
# # for x in pattern14.finditer(text_to_search):
# #     print(x)

# # '^' OUTSIDE THE CHARACTER SET MATCHES BEGINNING OF THE STRING INSIDE [] ACTS AS NOT
 
# # pattern14 = re.compile(r'[^a-zA-Z0-9]')
# # for x in pattern14.finditer(text_to_search):
# #     print(x)

# # pattern15 = re.compile(r'[^c]at')
# # for x in pattern15.finditer(text_to_search):
# #     print(x)

# # *       - 0 or More
# # +       - 1 or More
# # ?       - 0 or One
# # {3}     - Exact Number
# # {3,4}   - Range of Numbers (Minimum, Maximum)

# # pattern16 = re.compile('\d{3}[-.]\d{3}[-.]\d{4}')
# # for x in pattern16.finditer(text_to_search):
# #     print(x)

# # pattern17 = re.compile(r'Mr\.?\s[A-Z]\w*')
# # for x in pattern17.finditer(text_to_search):
# #     print(x)


# # pattern18 = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
# # for x in pattern18.finditer(text_to_search):
# #     print(x)


# # # returns a list containing all matches
# # txt = "The rain in Spain"
# # x = re.findall("ai", txt)
# # print(x)


# # # The search() function searches the string for a match, and returns a Match object if there is a match.

# # txt = "The rain in Spain"
# # x = re.search("\s", txt)

# # print("The first white-space character is located in position:", x.start())


# # # The split() function returns a list where the string has been split at each match:
# # txt = "The rain in Spain"
# # x = re.split("\s", txt)
# # print(x)



# # txt = "The rain in Spain"
# # x = re.sub("\s", "9", txt)
# # print(x)


# # txt = "The rain in Spain"
# # x = re.sub("\s", "9", txt, 2)
# # print(x)

# emails = '''
# CoreyMSchafer@gmail.com
# corey.schafer@university.edu
# corey-321-schafer@my-work.net
# '''


# pattern_email = re.compile(r'[\w.-]+@[\w.-]+\.\w+')

# for x in pattern_email.finditer(emails):
#     print(x)

# urls = '''
# https://www.google.com
# http://coreyms.com
# https://youtube.com
# https://www.nasa.gov
# '''

# pattern_url = re.compile(r'https?://(www\.)?\w+.(\.\w+)')
# for x in pattern_url.finditer(urls):
#     print(x)

txt = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789

ace    bad    cat    dry    eve
away   bent   crow   dove   ends
attic  brand  crypt  dried  event
annoys baller camera diving ethics
love glove move stove glOwve moves
aasad aaapron

decade decades
'''

print(txt)

# hey there How are you.
# Code Man's code is so efficient, he once saved a client $10,000 by deleting a single semicolon.
# In the heat of battle, Syntax Slayer would code so Furiously that his keyboard would catch fire.
# Regex Rex could spot a misplaced semicolon from a mile away, no problem.
# Hey there!
# At precisely 2:47PM, ByteBoy finished debugging his program and saved the company $1 million.
# With her lightning-fast typing skills, Keyboard Queen can code circles around her coworkers. Literally, she once wrote a program that made the computer screen display a rotating circle of text that read 'I'm faster than you'.
# The legendary programmer known only as 'Barbarian Bob' was feared by his colleagues for his ruthless coding style. He once wrote an algorithm that duplicated the word 'barbarian' 100 times, just to prove a point.
# Cash Coder never works for free. His hourly rate is $1,000. But don't worry, he's worth every penny. He once coded a program that made a toaster sing 'Sweet Child O' Mine' every time it popped.



KeItH sAyS yOu NeEd To LeArN rEgExEs

wElCoMe To ThE sAlTy SpItOoN, hOw ToUgH aRe YoU?

This is a boring, normal sentence.

lEt Me SeE tHaT sPoNgEbOb MeMe OnE mOrE tImE



MM-DD-YYYY (or MM.DD.YYYY -- MM/DD/YYYY)

06-04-2000
Christmas this year is 12/25/2023
32-22-2022
Humans first stepped on the moon July 20, 1969
10/31/99
A great movie came out on 02.16.1996


123456789
999000999
8712388411235

mississippi
bookkeeping
aggressive
words


1, 2, 3, 4, 5

$9 $12 $1,000 $10,000 $3 million
$60 trillion
9:30am 10am 1pm 7:45pm 11:20 PM 11:35 pm
