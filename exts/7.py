query = input("Search for: ")
upto = int(input("In range up to: "))

count = 0
for i in range(1, upto+1):
    if query in str(i):
        print(f"{i} contains {query}")
        count += 1

print(f"Found {count} number(s) containing {query} between 1 and {upto}")

