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
    if item in shop:
        if bits >= shop[item]["cost"]:
            bits -= shop[item]["cost"]
            items.append(shop[item])
            bps += shop[item]["bpt"]

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
                buy(shop[j])

    print("\n" * 80)
    print("Shop: ")
    for i, j in enumerate(shop):
        if i == selected:
            print(f'> {j}: {shop[j]["cost"]}')
        else:
            print(f'{j}: {shop[j]["cost"]}')

    print()
    print(f"bits: {bits}")
