class Student:
    def __init__(self, name_surname, group, grade):
        self.name_surname = name_surname
        self.group = group
        self.grade = grade

    def average_grade(self):
        return sum(self.grade) / len(self.grade)

    def info(self):
        return f"{self.name_surname}, {self.group}, средний балл: {self.average_grade():.2f}"

def get_average_grade(student):
    return student.average_grade()


student_catalog = []

for index in range(10):
    print(f"\n{index + 1} студент")
    name_surname_student = input("Введите Фамилию и имя студента: ")
    group_student = input("Введите название группы студента: ")

    grades = []
    for mark in range(5):
        grade = int(input(f"Введите {mark + 1} оценку: "))
        grades.append(grade)

    student = Student(name_surname_student, group_student, grades)
    student_catalog.append(student)


student_catalog.sort(key = get_average_grade)

for student in student_catalog:
    print(student.info())

