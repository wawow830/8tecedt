price = int(input("Price of computer: "))
depost = int(input("Amount of pocket depost: "))

months = 0
total = deposit
while total < price:
    total += deposit
    total *= 1.05
    months += 1

print(f"months: {months}")
print(f"total: {total}")
print(f"depost: {depost}")
print(f"price: {price}")

print(f"It will take {months} months to buy the computer.")
