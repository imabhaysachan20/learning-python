x = ('apple', 'banana', 'cherry')
y = enumerate(x)

print(y)

d = {"a": 10, "b": 20}
for i, (k, v) in enumerate(d.items()):
    print(i, k, v)

runner = ["Lenka", "Martina", "Gugu"]
for winner in enumerate(runner):
    print(winner)

runners = ["Lenka", "Martina", "Gugu"]
for position, name in enumerate(runners, start=1):
        print(position, name)