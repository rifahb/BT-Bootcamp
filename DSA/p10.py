def get_score(subject_name):
    while True:
        try:
            score = float(input(f"Enter marks for {subject_name} (0–100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def calculate_class(avg):
    if avg >= 60:
        return "1st Class"
    elif avg >= 50:
        return "2nd Class"
    elif avg >= 35:
        return "Pass Class"
    else:
        return "Fail"


def main():
    name = input("Enter student's name: ")

    s1 = get_score("Subject 1")
    s2 = get_score("Subject 2")
    s3 = get_score("Subject 3")
    total = s1 + s2 + s3
    avg = total / 3
    result_class = calculate_class(avg)
    print("\n===== STUDENT REPORT CARD =====")
    print("Name:", name)
    print("Total Marks:", total)
    print("Average Marks:", round(avg, 2))
    print("Class Secured:", result_class)
    print("================================")
main()
