students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def collect_student_data(students_dictionary):
    all_interests = []
    total_surname_length = 0

    for student_info in students_dictionary.values():
        all_interests.extend(student_info['interests'])
        total_surname_length += len(student_info['surname'])

    return set(all_interests), total_surname_length


student_info_pairs = [
    (student_id, student_info['age'])
    for student_id, student_info in students.items()
]

students_interests, students_surname_length = collect_student_data(students)

print("Список пар 'ID студента — возраст':", student_info_pairs)
print("Полный список интересов всех студентов:", students_interests)
print("Общая длина всех фамилий студентов:", students_surname_length)