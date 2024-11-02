class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []  # List to store enrolled students

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)  # Add the student to the course
            student.enroll_course(self)    # Enroll course in student record

    def display_course_info(self):
        print(f"Course Name: {self.course_name}")
        print(f"Course Code: {self.course_code}")
        print(f"Instructor: {self.instructor}")
        print("Enrolled Students:")
        for student in self.students:
            print(f"- {student.name} (ID: {student.student_id})")
