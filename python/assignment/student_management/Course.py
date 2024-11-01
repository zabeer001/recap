class Course:
    def __init__(self, course_name: str, course_code: str, instructor: str):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            student.enroll_course(self.course_code)

    def display_course_info(self):
        student_names = ', '.join(student.name for student in self.students) if self.students else 'No students enrolled'
        info = f"Course Name: {self.course_name}\n" \
               f"Course Code: {self.course_code}\n" \
               f"Instructor: {self.instructor}\n" \
               f"Enrolled Students: {student_names}"
        print(info)
