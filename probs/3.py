num = int(input("Input Number: "))
factors = [i for i in range(1, num+1) if num % i == 0]
print(f"The factors of {num} are:")
print(*factors, sep="\n")
