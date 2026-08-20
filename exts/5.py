word = input("Word: ")
hero = input("Hero: ")
repeat = int(input("Repeat: "))

print(f"{word}{word[-2:] * (repeat)} {hero}")
