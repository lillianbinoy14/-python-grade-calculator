# Simple Student Grade Calculator

name = input("Enter student name: ")

mark1 = float(input("Enter mark 1: "))
mark2 = float(input("Enter mark 2: "))
mark3 = float(input("Enter mark 3: "))

average = (mark1 + mark2 + mark3) / 3

print("\nStudent Name:", name)
print("Average Mark:", average)

if average >= 75:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: F")
