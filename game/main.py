bits = 0
bps = 0

items = []
available = []
selected = 0

shop = {
    "cursor": {
        "bps": 0.1,
        "cost": 10
    }
}

def getAvailable():
    global bits
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

def update():
    global bits, available
    bits += bps
    available = getAvailable()

def render():
    global available, bits
    print("\n" * 80)
    print(f"Shop: {available}")
    print(f"Bits: {bits}")

def click():
    global bits
    bits += 1

def select(x):
    global selected
    selected += x

while True:
    update()
    render()
