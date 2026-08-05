fname = "favourites.txt"
favs = []

with open(fname, "r") as file:
    next(file, None)
    for line in file:
        favs.append(line.strip())

print(f"Favourites count: {len(favs)}")
print(f"First item: {favs[0]}")
print(f"Last item: {favs[-1]}")
