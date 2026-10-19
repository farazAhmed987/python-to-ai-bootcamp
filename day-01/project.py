def analyze(marks):
    total = sum(marks)
    avg = total / len(marks)
    
    if avg > 90:
        print("Excellent")
    elif avg>70:
        print("Normal")
    elif avg > 50:
        print("Needs improvement")
    else:
        print("Bad Result")
        
    
    for i in range(0,4):
        print(marks[i])
    
    print("Total :", total)
    print("Avg: ", round(avg, 2))
    

student_marks = [40, 80, 90, 100, 50]

analyze(student_marks)

//practice

def analyze(marks):
    if not marks:
        print("No marks available.")
        return

    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        result = "Excellent"
    elif average >= 70:
        result = "Good"
    elif average >= 50:
        result = "Needs Improvement"
    else:
        result = "Poor Result"

    print("Student Marks Analysis")
    print("----------------------")
    print("Marks:", marks)
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
    print("Highest Marks:", max(marks))
    print("Lowest Marks:", min(marks))
    print("Result:", result)


student_marks = [40, 80, 90, 100, 50]
analyze(student_marks)
