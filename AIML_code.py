GRADE_POINTS = {
    "S": 10,
    "A": 9,
    "B": 8,
    "C": 7,
    "D": 6,
    "E": 5,
    "F": 0,
    "N": 0,
}


def get_positive_int(prompt):
    while True:
        value = input(prompt).strip()
        try:
            number = int(value)
            if number > 0:
                return number
        except ValueError:
            pass
        print("Please enter a valid positive whole number.")


def get_positive_float(prompt):
    while True:
        value = input(prompt).strip()
        try:
            number = float(value)
            if number > 0:
                return number
        except ValueError:
            pass
        print("Please enter a valid positive number.")


def get_float_in_range(prompt, minimum, maximum):
    while True:
        value = input(prompt).strip()
        try:
            number = float(value)
            if minimum <= number <= maximum:
                return number
        except ValueError:
            pass
        print(f"Please enter a value between {minimum} and {maximum}.")


def get_grade(prompt):
    while True:
        grade = input(prompt).strip().upper()
        if grade in GRADE_POINTS:
            return grade
        print("Enter a valid VIT grade: S, A, B, C, D, E, F, or N.")


def print_grade_table():
    print("\nVIT-style Grade Points Used")
    print("S = 10")
    print("A = 9")
    print("B = 8")
    print("C = 7")
    print("D = 6")
    print("E = 5")
    print("F = 0")
    print("N = 0")


def calculate_sgpa():
    print("\nSGPA CALCULATOR")
    subjects = get_positive_int("Enter number of subjects in the semester: ")

    total_credits = 0.0
    total_grade_points = 0.0

    for index in range(1, subjects + 1):
        print(f"\nSubject {index}")
        subject_name = input("Subject name: ").strip() or f"Subject {index}"
        credits = get_positive_float(f"Credits for {subject_name}: ")
        grade = get_grade(f"Grade for {subject_name}: ")

        total_credits += credits
        total_grade_points += credits * GRADE_POINTS[grade]

    sgpa = total_grade_points / total_credits

    print("\nRESULT")
    print(f"Total credits: {total_credits:.2f}")
    print(f"Total grade points: {total_grade_points:.2f}")
    print(f"SGPA: {sgpa:.2f}")


def calculate_cgpa_from_semesters():
    print("\nCGPA CALCULATOR FROM SEMESTERS")
    semesters = get_positive_int("Enter number of completed semesters: ")

    total_credits = 0.0
    total_weighted_points = 0.0

    for semester in range(1, semesters + 1):
        print(f"\nSemester {semester}")
        sgpa = get_float_in_range("Enter semester SGPA: ", 0, 10)
        credits = get_positive_float("Enter semester credits: ")

        total_credits += credits
        total_weighted_points += sgpa * credits

    cgpa = total_weighted_points / total_credits

    print("\nRESULT")
    print(f"Total credits counted: {total_credits:.2f}")
    print(f"Total weighted points: {total_weighted_points:.2f}")
    print(f"CGPA: {cgpa:.2f}")
    print(f"Approximate percentage: {cgpa * 10:.2f}%")


def calculate_cgpa_from_courses():
    print("\nCGPA CALCULATOR FROM COURSE GRADES")
    semesters = get_positive_int("Enter number of semesters to include: ")

    total_credits = 0.0
    total_grade_points = 0.0

    for semester in range(1, semesters + 1):
        print(f"\nSemester {semester}")
        subjects = get_positive_int("Enter number of subjects in this semester: ")

        for subject_index in range(1, subjects + 1):
            print(f"\nSemester {semester} - Subject {subject_index}")
            subject_name = input("Subject name: ").strip() or f"Subject {subject_index}"
            credits = get_positive_float(f"Credits for {subject_name}: ")
            grade = get_grade(f"Grade for {subject_name}: ")

            total_credits += credits
            total_grade_points += credits * GRADE_POINTS[grade]

    cgpa = total_grade_points / total_credits

    print("\nRESULT")
    print(f"Total credits counted: {total_credits:.2f}")
    print(f"Total grade points: {total_grade_points:.2f}")
    print(f"CGPA: {cgpa:.2f}")
    print(f"Approximate percentage: {cgpa * 10:.2f}%")


def main():
    print("VIT Bhopal CGPA Calculator")
    print("This uses the common VIT 10-point grade mapping.")
    print_grade_table()

    print("\nChoose an option:")
    print("1. Calculate SGPA from subject grades")
    print("2. Calculate CGPA from semester SGPAs")
    print("3. Calculate CGPA directly from all course grades")

    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        calculate_sgpa()
    elif choice == "2":
        calculate_cgpa_from_semesters()
    elif choice == "3":
        calculate_cgpa_from_courses()
    else:
        print("Invalid choice. Please run the program again and enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
