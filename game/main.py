bits = 0
bpt = 0
items = []
selected = 0

shop = {
    "biter": {
        "cost": 8,
        "bpt": 1
    },
    "basher": {
        "cost": 64,
        "bpt": 16
    }
}

def buy(item):
    global bits, bpt
    if str(item) in shop:
        if bits >= shop[item]["cost"]:
            bits -= shop[item]["cost"]
            items.append(shop[item])
            bpt += shop[item]["bpt"]

def select(x):
    global selected
    selected += x
    selected = selected % len(shop)

inp = ""
while True:
    inp = input()
    if inp == "":
        bits += 1

    if inp == "up":
        select(1)
    if inp == "down":
        select(-1)

    if inp == "buy":
        for i, j in enumerate(shop):
            if i == selected:
                buy(j)

    bits  += bpt

    print("\n" * 80)
    print("Shop: ")
    for i, j in enumerate(shop):
        if i == selected:
            print(f'> {j}: {shop[j]["cost"]} bits, {shop[j]["bpt"]} bpt')
        else:
            print(f'{j}: {shop[j]["cost"]} bits, {shop[j]["bpt"]} bpt')

    print()
    print(f"bits: {bits}")
