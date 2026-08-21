price = int(input("Price of computer: "))
deposit = int(input("Amount of pocket deposit: "))

months = 0
total = deposit
while total < price:
    total += deposit
    total *= 1.05
    months += 1

if months > 0:
    print(f"It will take {months} months to buy the computer.")
else:
    print("You have enough money to buy the computer now!")
