studentCount = 5
fname = "classMembers.txt"

students = [input(f"Student {studentIter}'s name: ").title() for studentIter in range(1, studentCount +1)]

with open(fname, "w") as file:
    file.writelines(f"{student}\n" for student in students)

#------------------------------------------------------------

roll = []

with open(fname, "r") as file:
    roll = [line.strip() for line in file]

print("Students saved:\n")
print(*(f"{i}. {j}" for i, j in enumerate(roll, start=1)), sep="\n")
print(f"\nTotal students: {len(roll)}")
