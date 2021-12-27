class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.all_courses_grades = []

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avrg_grade(self, grades, all_courses_grades):
        for grades in grades.values():
            avrg = sum(grades) / len(grades)
            all_courses_grades += [avrg]
        avrg = round(sum(all_courses_grades) / len(all_courses_grades), 2)
        return avrg

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}' \
              f'\nСредняя оценка за домашние задания: {self.avrg_grade(self.grades, self.all_courses_grades)}' \
              f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не является лектором!')
            return
        return self.avrg_grade(self.grades, self.all_courses_grades) < other.avrg_grade(other.grades,
                                                                                        other.all_courses_grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.all_courses_grades = []


class Lecturer(Mentor):
    def avrg_grade(self, grades, all_courses_grades):
        for grades in grades.values():
            avrg = sum(grades) / len(grades)
            all_courses_grades += [avrg]
        avrg = round(sum(all_courses_grades) / len(all_courses_grades), 2)
        return avrg

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: ' \
              f'{self.avrg_grade(self.grades, self.all_courses_grades)}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не является студентом!')
            return
        return self.avrg_grade(self.grades, self.all_courses_grades) < other.avrg_grade(other.grades,
                                                                                        other.all_courses_grades)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res


def avrg_grade_student_by_course(students, course):
    all_students_grades = []
    for student in students:
        if isinstance(student, Student) and course in student.courses_in_progress:
            for course_name, grade in student.grades.items():
                if course_name == course:
                    all_students_grades += grade
    all_students_grades = sum(all_students_grades) / len(all_students_grades)
    return all_students_grades


def avrg_grade_lecturer_by_course(lecturers, course):
    all_lecturer_grades = []
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            for course_name, grade in lecturer.grades.items():
                if course_name == course:
                    all_lecturer_grades += grade
    all_lecturer_grades = sum(all_lecturer_grades) / len(all_lecturer_grades)
    return all_lecturer_grades


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'JavaScript', 'Git']
best_student.finished_courses += ['Введение']

best_student2 = Student('Less', 'Name', 'your_gender')
best_student2.courses_in_progress += ['Python', 'JavaScript', 'Git']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Git']

cool_reviewer2 = Reviewer('Any', 'Body')
cool_reviewer2.courses_attached += ['Python', 'JavaScript']

best_lecturer = Lecturer('Lec', 'Turer')
best_lecturer.courses_attached += ['Python', 'JavaScript']

best_lecturer2 = Lecturer('Pro', 'Fessor')
best_lecturer2.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Git', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student2, 'Git', 10)
cool_reviewer.rate_hw(best_student2, 'Python', 10)

cool_reviewer2.rate_hw(best_student, 'Python', 10)
cool_reviewer2.rate_hw(best_student, 'JavaScript', 9)
cool_reviewer2.rate_hw(best_student2, 'Python', 9)
cool_reviewer2.rate_hw(best_student2, 'JavaScript', 9)

best_student.rate_lecturer(best_lecturer, 'Python', 10)
best_student2.rate_lecturer(best_lecturer, 'Python', 8)
best_student.rate_lecturer(best_lecturer, 'JavaScript', 10)
best_student2.rate_lecturer(best_lecturer, 'JavaScript', 9)
best_student.rate_lecturer(best_lecturer2, 'Git', 9)
best_student2.rate_lecturer(best_lecturer2, 'Git', 8)

students_list = [best_student, best_student2]
lecturer_list = [best_lecturer, best_lecturer2]

print(best_student.avrg_grade(best_student.grades, best_student.all_courses_grades))
print(best_student2.avrg_grade(best_student2.grades, best_student2.all_courses_grades))
print(best_lecturer.avrg_grade(best_lecturer.grades, best_lecturer.all_courses_grades))
print(best_lecturer2.avrg_grade(best_lecturer2.grades, best_lecturer2.all_courses_grades))

print(best_student)
print(best_student2)

print(cool_reviewer)
print(cool_reviewer2)

print(best_lecturer)
print(best_lecturer2)

print(best_student < best_lecturer)
print(best_student < best_lecturer2)
print(best_student2 < best_lecturer)
print(best_student2 < best_lecturer2)

print(avrg_grade_student_by_course(students_list, 'Python'))
print(avrg_grade_student_by_course(students_list, 'JavaScript'))
print(avrg_grade_student_by_course(students_list, 'Git'))

print(avrg_grade_lecturer_by_course(lecturer_list, 'Python'))
print(avrg_grade_lecturer_by_course(lecturer_list, 'JavaScript'))
print(avrg_grade_lecturer_by_course(lecturer_list, 'Git'))
