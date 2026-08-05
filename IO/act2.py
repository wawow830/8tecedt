fname = "favourites.txt"

favs = ["pizza", "code", "video games", "pop tarts"]
favs[:] = [fav.title() for fav in favs]

with open(fname, "w") as file:
    file.write("my favs:\n")
    file.writelines(f"{fav}\n" for fav in favs)
