fname = "welcome.txt"

name = "warren"
className = "8TECE"
interest = "software development"

line = f"My name is {name}. I am in {className}. I enjoy {interest}"

with open(fname, "w") as f:
    f.write(line)
