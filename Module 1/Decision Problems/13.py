
percentage = float(input("Enter the percentage of marks: "))

if percentage >= 90:
    grade = "O (Outstanding)"
elif percentage >= 85:
    grade = "A+ (Excellent)"
elif percentage >= 80:
    grade = "A (Very Good)"
elif percentage >= 70:
    grade = "B+ (Good)"
elif percentage >= 60:
    grade = "B (Above Average)"
elif percentage >= 50:
    grade = "C (Average)"
elif percentage >= 45:
    grade = "P (Pass)"
else:
    grade = "F (Fail)"

print("Percentage:", percentage)
print("Grade:", grade)





#output
#Enter the percentage of marks: 80
#Percentage: 80.0
#Grade: A (Very Good)