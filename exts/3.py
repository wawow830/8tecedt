people = int(input("Number of people: "))
cookies = int(input("Number of cookies: "))

cpp = int(cookies/people)
crtj = cookies % people

print(f"Cookies per person: {cpp}")
print(f"Cookies returning to jar: {crtj}")
