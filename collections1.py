def gradeLetter(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    studentname = input("Enter Student Name: ")

    grade1 = float(input("Enter Grade 1: "))
    grade2 = float(input("Enter Grade 2: "))
    grade3 = float(input("Enter Grade 3: "))
    grade4 = float(input("Enter Grade 4: "))
    grade5 = float(input("Enter Grade 5: "))

    grades = [grade1, grade2, grade3, grade4, grade5]

    average = sum(grades) / len(grades)

    print("Student:", studentname)
    print("Average:", average)

    letter_grade = gradeLetter(average)
    print("Letter Grade:", letter_grade)

main()