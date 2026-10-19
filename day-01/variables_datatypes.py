# print("hello world!")
# # print(var)

# # comments

# # print("akif 1")
# # print("akif 1")
# # print("akif 1")

# # int var = 1;
# # var = "akif" // assignment operator 

# # == //comparison operator
# # no = 1
# # dec = 1.5

# VAR = ".."

# # print(type(no))

# # no = float(input("enter a no :")) # string
# # print(no)
# # print(type(no))

# # += // pre 
# # =+ // post 

# # conditional statements

# # num = int(input("enter a value: "))

# # # -2, -1, 0, 1, 2
# # if num > 0:
# #     print("positive")
# # elif num < 0:
# #     print("negitive number")
# # else:
# #     print("the number is ZERO!")
    
    
# for i in range(1,6,2):
#     print(i)
# count = 1     0   =  0    + 1 => 0 = 1
# cont += 1 , count = count + 1

# left (variable --> count) = right (value), 1 
# count = 1

# name = "akif"

for number in range(1,8):
    if number == 2:
        continue
    if number == 5:
        break
    print(number)


//practice

name = "Akif"
age = 20
marks = 85.5
is_enrolled = True
graduation_year = None

print("Name:", name, "| Type:", type(name).__name__)
print("Age:", age, "| Type:", type(age).__name__)
print("Marks:", marks, "| Type:", type(marks).__name__)
print("Enrolled:", is_enrolled, "| Type:", type(is_enrolled).__name__)
print("Graduation Year:", graduation_year)

# Type conversion
age_next_year = int(age) + 1
print("Age Next Year:", age_next_year)

# Arithmetic and comparison operators
print("Total Marks After Bonus:", marks + 5)
print("Passed:", marks >= 50)
print("Eligible:", age >= 18 and is_enrolled)

# Loop with continue and break
for number in range(1, 8):
    if number == 2:
        continue
    if number == 6:
        break
    print("Number:", number)
