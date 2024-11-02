from Person import Person  # Import the Person class

class Student(Person):
    def __init__(self, name, age, address, student_id, grades=None, courses=None):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = grades if grades is not None else {}  # Default to empty dictionary
        self.courses = courses if courses is not None else []  # Default to empty list

   
    def add_grade(self, course_code: str, grade: str):
        if course_code in self.courses:
            self.grades[course_code] = grade
        else:
            print(f"Error: Student {self.name} is not enrolled in {course_code}.")

    def enroll_course(self, course_code: str):
        if course_code not in self.courses:
            self.courses.append(course_code)

    def display_student_info(self):
        courses = ', '.join(self.courses) if self.courses else 'None'
        grades = ', '.join([f"{course}: {grade}" for course, grade in self.grades.items()]) if self.grades else 'No grades available'
        info = f"Student ID: {self.student_id}\n" \
               f"Name: {self.name}\n" \
               f"Age: {self.age}\n" \
               f"Address: {self.address}\n" \
               f"Enrolled Courses: {courses}\n" \
               f"Grades: {grades}"
        print(info)