fname = "favourites.txt"
favs = []

with open(fname, "r") as file:
    next(file, None)
    for line in file:
        favs.append(line.strip())

print(f"Favourites count: {len(favs)}")
print(f"First item: {favs[0]}")
print(f"Last item: {favs[-1]}")

print()

print(*(f"{i}. {j}" for i, j in enumerate(favs, start=1)), sep="\n")

query = input("Enter an item to search for: ").title()
if query in favs:
    print(f"{query} was found in the file.")
else:
    print(f"{query} was not found in the file.")
