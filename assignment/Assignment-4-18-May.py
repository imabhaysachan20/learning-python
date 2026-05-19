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

#approach 1
ans = []
for x in unique:
    ans.append([x,data.count(x)])

print(ans)

#approach 2
arr2 = data.copy()
arr2.sort()
ans = list()
count = 1
for i in range(len(arr2)-1):
    if arr2[i]==arr2[i+1]:
        count += 1
    else:
        ans.append([arr2[i], count])
        count = 1

    print(i)

ans.append([arr2[i+1], count])

print(ans)