class Student:
    all_courses_grades = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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
        avrg = sum(all_courses_grades) / len(all_courses_grades)
        return avrg

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}' \
              f'\nСредняя оценка за домашние задания: {self.avrg_grade(self.grades, self.all_courses_grades)}' \
              f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
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


class Lecturer(Mentor):
    grades = {}
    avrg = 0
    all_courses_grades = []

    def avrg_grade(self, grades, all_courses_grades):
        for grades in grades.values():
            avrg = sum(grades)/len(grades)
            all_courses_grades += [avrg]
        avrg = sum(all_courses_grades)/len(all_courses_grades)
        return avrg

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: ' \
              f'{self.avrg_grade(self.grades, self.all_courses_grades)}'
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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'JavaScript']
best_student.finished_courses += ['Git']

best_student2 = Student('Less', 'Name', 'your_gender')
best_student2.courses_in_progress += ['Python', 'JavaScript']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'JavaScript']

best_lecturer = Lecturer('Lec', 'Turer')
best_lecturer.courses_attached += ['Python', 'JavaScript']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'JavaScript', 8)
cool_reviewer.rate_hw(best_student2, 'Python', 9)
cool_reviewer.rate_hw(best_student2, 'JavaScript', 10)

best_student.rate_lecturer(best_lecturer, 'Python', 10)
best_student2.rate_lecturer(best_lecturer, 'Python', 10)
best_student.rate_lecturer(best_lecturer, 'JavaScript', 9)
best_student2.rate_lecturer(best_lecturer, 'JavaScript', 9)

print(best_student.grades)

print(best_student2.grades)

print(best_lecturer.grades)

print(cool_reviewer)

print(best_lecturer)

print(best_student)

print(best_student.avrg_grade(best_student.grades, best_student.all_courses_grades))

print(best_lecturer.avrg_grade(best_lecturer.grades, best_lecturer.all_courses_grades))

print(best_student < best_lecturer)
