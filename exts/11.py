power = int(input("Enter power level: "))

for i in range(power, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
