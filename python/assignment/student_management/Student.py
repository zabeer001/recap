from Person import Person

class Student(Person):
    def __init__(self, name: str, age: int, address: str, student_id: str):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject: str, grade: str):
        self.grades[subject] = grade

    def enroll_course(self, course: str):
        if course not in self.courses:
            self.courses.append(course)

    def display_student_info(self):
        courses = ', '.join(self.courses) if self.courses else 'None'
        grades = self.grades if self.grades else 'No grades available'
        info = f"Student ID: {self.student_id}\n" \
               f"Name: {self.name}\n" \
               f"Age: {self.age}\n" \
               f"Address: {self.address}\n" \
               f"Enrolled Courses: {courses}\n" \
               f"Grades: {grades}"
        print(info)

# Example usage
if __name__ == "__main__":
    student1 = Student("Alice Smith", 20, "456 Elm St", "S12345")
    student1.enroll_course("Math")
    student1.add_grade("Math", "A")
    student1.add_grade("Science", "B")
    student1.display_student_info()
