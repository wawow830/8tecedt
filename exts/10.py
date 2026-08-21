cams = []

while len(cams) < 3:
    stock = input("Shop Stock: ")
    if "cam".casefold() in stock.casefold():
        cams.append(stock.title())

cams.sort(reverse=True)
print(f"Proposals: {", ".join(cams)}")
