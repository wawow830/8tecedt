name1 = input("Name 1: ")
name2 = input("Name 2: ")

if len(name1) == len(name2):
    if name1 == name2:
        print("The names are the same.")
    else:
        print("The names are different, but are the same length.")
else:
    if len(name1) > len(name2):
        print(f"{name1} has a longer name than {name2}")
    else:
        print(f"{name2} has a longer name than {name1}")
