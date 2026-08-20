text = input("Line: ")

result = ""

for ch in text:
    if ch in "aeiou":
        result += ch + "f" + ch
    else:
        result += ch

print(result)
