bits = 0
bpt = 0
items = []
selected = 0

shop = {
    "biter": {
        "cost": 8,
        "bpt": 1
    }
}

def buy(item):
    if item in shop:
        if bits >= shop[item]["cost"]:
            bits -= shop[item]["cost"]
            items.append(shop[item])

inp = ""
while True:
    inp = input()
    if inp == "":
        bits += 1

    if inp == "up"
        selected += 1
    if inp == "down"
        selected -= 1

    print("\n" * 80)
    print("Shop: ")
    for i, j in enumerate(shop):
        if i == selected:
            print(f'> {j}: {shop[j]["cost"]}')
        else:
            print(f'{j}: {shop[j]["cost"]}')

    print()
    print(f"bits: {bits}")
