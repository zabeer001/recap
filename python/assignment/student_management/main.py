import json
from Student import Student
from Course import Course

students = []
courses = []

def load_data():
    global students, courses
    try:
        with open("students.json", "r") as f:
            students = [Student(**data) for data in json.load(f)]
    except FileNotFoundError:
        print("No existing student data found. Starting fresh.")
    except json.JSONDecodeError:
        print("Error reading student data. Starting fresh.")

    try:
        with open("courses.json", "r") as f:
            courses = [Course(**data) for data in json.load(f)]
    except FileNotFoundError:
        print("No existing course data found. Starting fresh.")
    except json.JSONDecodeError:
        print("Error reading course data. Starting fresh.")

def save_data():
    with open("students.json", "w") as f:
        json.dump([s.__dict__ for s in students], f)

    with open("courses.json", "w") as f:
        json.dump([{"course_name": c.course_name, "course_code": c.course_code, "instructor": c.instructor, "students": [s.student_id for s in c.students]} for c in courses], f)

def add_student():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    address = input("Enter student's address: ")
    student_id = input("Enter student ID: ")
    student = Student(name, age, address, student_id)
    students.append(student)
    print(f"Student {name} added successfully.")

def enroll_in_course():
    student_id = input("Enter student ID: ")
    course_code = input("Enter course code: ")
    student = next((s for s in students if s.student_id == student_id), None)
    course = next((c for c in courses if c.course_code == course_code), None)
    
    if student and course:
        course.add_student(student)
        print(f"Student {student.name} enrolled in {course.course_name} successfully.")
    else:
        print("Student or course not found.")

def add_grade():
    student_id = input("Enter student ID: ")
    course_code = input("Enter course code: ")
    grade = input("Enter grade: ")
    student = next((s for s in students if s.student_id == student_id), None)
    
    if student:
        student.add_grade(course_code, grade)
        print(f"Grade {grade} added for student {student.name} in {course_code}.")
    else:
        print("Student not found.")

def display_student_details():
    student_id = input("Enter student ID: ")
    student = next((s for s in students if s.student_id == student_id), None)
    
    if student:
        student.display_student_info()
    else:
        print("Student not found.")

def display_course_details():
    course_code = input("Enter course code: ")
    course = next((c for c in courses if c.course_code == course_code), None)

    if course:
        course.display_course_info()
    else:
        print("Course not found.")

def main():
    load_data()
    
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Enroll in Course")
        print("3. Add Grade")
        print("4. Display Student Details")
        print("5. Display Course Details")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            enroll_in_course()
        elif choice == '3':
            add_grade()
        elif choice == '4':
            display_student_details()
        elif choice == '5':
            display_course_details()
        elif choice == '6':
            save_data()
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
