import re
# text = "Contact us at support@test.com or admin123@gmail.com"

# pattern = re.compile(r'[\w.-]+@[\w.-]+\.\w+')
# for x in pattern.finditer(text):
#     print(x)

# DD-MM-YYYY
# DD/MM/YYYY
# YYYY-MM-DD




# text = "Meeting on 12-05-2026 and another on 2026-06-01"

# pat1 = re.compile(r'\d{2,4}[-/]\d{2}[-/]\d{2,4}')
# for x in pat1.finditer(text):
#     print(x)

# text = "This is is a sample sample text."

# 2. Validate Password
# Write a regex to validate a password that must:
# Be at least 8 characters
# Contain at least 1 uppercase letter
# Contain at least 1 lowercase letter
# Contain at least 1 digit
# Contain at least 1 special character

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'

passwords = [
    "Password@123",
    "password123",
    "PASSWORD@123",
    "Password123",
    "Pass@1"
]

for password in passwords:
    if re.fullmatch(pattern, password):
        print(f"{password} -> Valid")
    else:
        print(f"{password} -> Invalid")

# pat2 = re.compile(r'\b(\w+)\s+\1\b')
# for x in pat2.finditer(pat2):
#     print(x)


# text = "Hello     World\t\tPython"
# text = re.sub(r'\s+',' ',text)

# print(text)

    


text = '''<div>Hello</div>
<p>World</p>
<a href="#">Link</a>Give feedback'''

patter = r'<\s*([a-zA-Z]+)'



print(re.findall(patter,text))

text = '''
"Revenue was $1,200.50, profit ₹50,000 and loss €300"'''

print(re.findall(r'[$₹€]([\d,]+(?:\.\d+)?)',text))



text = '''
2026-06-01 10:23:45 ERROR Database connection failed
2026-06-01 10:24:12 INFO User login successful'''

date_pattern = r'\d{4}-\d{2}-\d{2}'
time_pattern = r'\d{2}:\d{2}:\d{2}'
msg_pattern = r'(?<=\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})[\w\s]+'

print(re.findall(date_pattern,text))
print(re.findall(time_pattern,text))
print(re.findall(msg_pattern,text))