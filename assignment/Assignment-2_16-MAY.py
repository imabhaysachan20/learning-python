def twoSum(target,lst):
    ans = set()
    for x in range(len(lst)):
        for y in range(x,len(lst)):
            if lst[x] + lst[y] == target:
                ans.add((lst[x],lst[y]))
    print(tuple(ans))

def twoSum2(target,lst):
    mp = set()
    ans = []
    for x in lst:
        new_target = target-x
        if (new_target in mp):
            ans.append((x,new_target))
        mp.add(x)
    print(tuple(ans))


twoSum(9,[1,2,3,4,5,6,7,8])
twoSum2(9,[1,2,3,4,5,6,7,8])