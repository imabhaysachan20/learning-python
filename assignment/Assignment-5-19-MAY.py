students = {
    "Rahul": 85,
    "Sneha": 67,
    "Amit": 67,
    "John": 45

}

# Find topper
max = -1e9
ans = ""
for x in students:
    if(students[x]>max):
        max = students[x]
        ans = x
print(ans)

# Find failed students (<50)
ans = []
for x in students:
    if(students[x]<50):
        ans.append(x)
print(ans)

# Find students with same marks
map_dict = {}
for key,value in students.items():
    map_dict.setdefault(value, []).append(key)
res = {k:v for k,v in map_dict.items() if len(v)>1}
print(res)

# Print grades
for x in students:
    print(students[x])

# Merge and sort dictionary both by key and value

##by key
d1 = {"a": 1, "b": 4}
d2 = {"c": 3, "d": 4}
d2.update(d1)
print(dict(sorted(d2.items())))
## by value
print(dict(sorted(d2.items(),key=lambda x:x[1])))

