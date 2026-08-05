fname = "favourites.txt"

contents = ''

with open(fname, "r") as file:
    contents = file.read()

print(contents)
