said = input("What did you say? ")

while said.casefold() != "i love brussel sprouts!".casefold():
    print(said.upper())
    said = input("What did you say? ")

print("You're no fun.")
