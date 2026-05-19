python_students = {"Rahul","Amit","Sneha","John"}
sql_students = {"John","Sneha","David","Meena"}
aws_students = {"Rahul","David","Kiran"}

#Students in both Python and SQL
python_sql_student = python_students.intersection(sql_students)
python_sql_student2 = python_students & sql_students
print(python_sql_student)
print(python_sql_student2)


# Students in all 3 courses
all_student = python_students.union(sql_students).union(aws_students)
all_student2 = python_students | sql_students | aws_students
print(all_student2)


# Students only in Python
print(python_students-(sql_students|aws_students))


#Total unique students
print(len(all_student))


# Students not enrolled in AWS
not_aws = (python_students.union(sql_students))-aws_students
print(not_aws)


# students in more than 2 courses
result = python_students & sql_students & aws_students
print(result)

#student whose name start with 'Ra'

lst = []
for x in all_student:
    if(x.lower().startswith('ra')):
        lst.append(x)

print(lst)  

#student whose name end with 'an' or 'na'
lst = []
for x in all_student:
    if(x.lower().endswith('an') or x.lower().endswith('na`')):
        lst.append(x)

print(lst)  

    