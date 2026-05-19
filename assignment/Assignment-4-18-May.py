data = [1,2,2,3,4,4,4,5]

#unique value
unique = list(set(data))
print(unique)

#duplicate values
setContainer = set()
answer = set()
for x in data:
    if x in setContainer:
        answer.add(x)
    setContainer.add(x)

print(list(answer))

#freq of each elem
ans = []
for x in unique:
    ans.append([x,data.count(x)])

print(ans)