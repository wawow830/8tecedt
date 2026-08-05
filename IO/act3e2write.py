fname = "subjects.txt"

subjects = ["English", "Math", "Science", "History", "Geography", "TAS"]

with open(fname, 'w') as file:
    file.write("Subjects:\n")
    file.writelines(f"{subject}\n" for subject in subjects)
