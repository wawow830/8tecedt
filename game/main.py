bits = 0
bps = 0

items = []
available = []

shop = {
    "cursor": {
        "bps": 0.1,
        "cost": 10
    }
}

def getAvailable():
    return [
        name
        for name, item in shop.items()
        if item["cost"] <= bits
    ]

def computeBps():
    global bps
    bps = 0
    for item in items:
        bps += item["bps"]

def buy(item):
    global bits
    if item in available:
        bits -= shop[item]["cost"]
        items.append(shop[item])
        computeBps()

def click():
    global bits
    if input() == "":
        bits += 1

def update():
    global bits, available
    bits += bps
    available = getAvailable()

def render():
    print("\n" * 80)
    print(f"Shop: {available}")
    print(f"Bits: {bits}")


while True:
    click()
    update()
    render()
