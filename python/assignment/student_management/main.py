from Student import Student
from Course import Course

# Store students and courses in dictionaries for easy retrieval by ID or course code
students = {}
courses = {}

def add_student():
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    address = input("Enter Student Address: ")
    student_id = input("Enter Student ID: ")
    student = Student(name, age, address, student_id)
    students[student_id] = student
    print(f"Student '{name}' added successfully.")

def add_course():
    course_name = input("Enter Course Name: ")
    course_code = input("Enter Course Code: ")
    instructor = input("Enter Instructor Name: ")
    course = Course(course_name, course_code, instructor)
    courses[course_code] = course
    print(f"Course '{course_name}' added successfully.")

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Add New Course")
        print("3. Enroll in Course")
        print("4. Add Grade")
        print("5. Display Student Details")
        print("6. Display Course Details")
        print("0. Exit")
        
        option = input("Select Option: ")
        
        if option == "1":
            add_student()
        elif option == "2":
            add_course()
        elif option == "3":
            enroll_in_course()
        elif option == "4":
            add_grade()
        elif option == "5":
            display_student_details()
        elif option == "6":
            display_course_details()
        elif option == "0":
            print("Exiting the system.")
            break
        else:
            print("Invalid option. Please try again.")

def enroll_in_course():
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")
    student = students.get(student_id)
    course = courses.get(course_code)
    
    if student and course:
        course.add_student(student)
        print(f"Student {student.name} enrolled in {course.course_name}.")
    else:
        print("Invalid student ID or course code.")

def add_grade():
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")
    grade = input("Enter Grade: ")
    student = students.get(student_id)
    
    if student and course_code in [course.course_code for course in student.courses]:
        student.add_grade(course_code, grade)
        print(f"Grade {grade} added for {student.name} in course {course_code}.")
    else:
        print("Student is not enrolled in this course.")

def display_student_details():
    student_id = input("Enter Student ID: ")
    student = students.get(student_id)
    
    if student:
        student.display_student_info()
    else:
        print("Student not found.")

def display_course_details():
    course_code = input("Enter Course Code: ")
    course = courses.get(course_code)
    
    if course:
        course.display_course_info()
    else:
        print("Course not found.")

if __name__ == "__main__":
    main()
