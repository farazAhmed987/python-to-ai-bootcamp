# skills = ["Ml", "Python", "Numpy"]

# # # print(skills[2])

# # skills[2] = "Pandas"
# # print(skills[2])

# # print(len(skills))

# # print("maths" not in skills)

# # skills.append("Maths")
# # print(skills)

# # skills.extend(["Calculus", "Stats", "Prob"])
# # print(skills)

# num = [10,30,20]
# sorted_num = sorted(num)
# print(sorted_num)

student = {
    "name": "Akif",
    "age": 20,
    "gpa": 3.94
}

# for key, value in student.items():
#     print(key, ":", value)
    
print(student.get("age"))
print(student.keys())
print(student.values())

// practice

skills = ["Python", "Machine Learning", "NumPy"]

skills.append("Pandas")
skills.extend(["Statistics", "Data Analysis"])

print("Available Skills:", skills)
print("Total Skills:", len(skills))

student = {
    "name": "Akif",
    "age": 20,
    "gpa": 3.94,
    "skills": skills
}

print("Student Name:", student.get("name"))
print("Student GPA:", student.get("gpa"))
print("Student Skills:")

for skill in student["skills"]:
    print("-", skill)
