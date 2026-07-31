fooList = []

with open('foo.txt', "r") as file:
    for l in file:
        fooList.append(l)

print(fooList)
