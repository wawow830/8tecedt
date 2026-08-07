bits = 0
bpt = 0
items = []

shop = {
    "biter" {
        "cost": 8,
        "bpt": 1
    }
}

def buy(item):
    if item in shop:
        if bits >= shop[item]["cost"]:
            bits -= shop[item]["cost"]
            items.append(shop[item])

while True:
    if input() == "":
        bits += 1

    print("\n" * 80)
    print("Shop: ")
    for name, item in shop:
        print(f"{name}: {item["cost"]}")
    print(f"bits: {bits}")
