class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def student_average_grade(self, student_name):
        for student in self.students:
            if student.name == student_name:
                return student.average_grade()

        return None

    def course_average_grade(self):
        grades_sum = 0
        num_grades = 0

        for student in self.students:
            grades_sum += sum(student.grades)
            num_grades += len(student.grades)

        return grades_sum / num_grades


class Report:
    def __init__(self, course):
        self.course = course

    def student_report(self, student_name):
        student_avg_grade = self.course.student_average_grade(student_name)

        if student_avg_grade is None:
            return f"Student '{student_name}' not found in course '{self.course.course_name}'"

        return f"Student '{student_name}' average grade in course '{self.course.course_name}' is {student_avg_grade:.2f}"

    def course_report(self):
        return f"Course '{self.course.course_name}' average grade is {self.course.course_average_grade():.2f}"


def main():
    math_course = Course("Math")

    student1 = Student("John")
    student1.add_grade(80)
    student1.add_grade(90)
    student1.add_grade(95)

    student2 = Student("Jane")
    student2.add_grade(70)
    student2.add_grade(85)
    student2.add_grade(90)

    math_course.add_student(student1)
    math_course.add_student(student2)

    report = Report(math_course)

    print(report.student_report("John"))
    print(report.course_report())

if __name__ == '__main__':
    main()
