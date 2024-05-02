#Задание №4

#average_student(StudentGrades) - функция подсчета среднего значения оценки студентов
def average_student(StudentGrades):
    all_grades = []
    for courses in StudentGrades:
        all_grades += StudentGrades[courses]
    if len(all_grades) > 0:
        average_grade_student = sum(all_grades) / len(all_grades)
    else:
        average_grade_student = 0
    return average_grade_student

#average_lecturer(LecturerGrades)- функция подсчета среднего значения оценки лекторов
def average_lecturer(LecturerGrades):
    all_grades = []
    for courses in LecturerGrades:
        all_grades += LecturerGrades[courses]
    if len(all_grades) > 0:
        average_grade_lecturer = sum(all_grades) / len(all_grades)
    else:
        average_grade_lecturer = 0
    return  average_grade_lecturer
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade_student = [0]  # переменная для передачи в класс средней оценки студентов из функции average_student(StudentGrades)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade_student[0]}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {', '.join(self.finished_courses)}\n')

    def __eq__(self, other):
            return self.average_grade_student[0] == other.average_grade_student[0]

    def __lt__(self, other):
            return self.average_grade_student[0] < other.average_grade_student[0]

    def __gt__(self, other):
            return self.average_grade_student[0] > other.average_grade_student[0]

    def __ne__(self, other):
            return self.average_grade_student[0] != other.average_grade_student[0]

    def __le__(self, other):
            return self.average_grade_student[0] <= other.average_grade_student[0]

    def __ge__(self, other):
            return self.average_grade_student[0] >= other.average_grade_student[0]

    # функция rate_lec() - это функция оценки лекторов студентами.
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}
        self.average_grade_lecturer = [0] # переменная для передачи в класс средней оценки лекторов из функции  average_lecturer(LecturerGrades)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade_lecturer[0]}\n')

    def __eq__(self, other):
        return self.average_grade_lecturer[0] == other.average_grade_lecturer[0]

    def __lt__(self, other):
        return self.average_grade_lecturer[0] < other.average_grade_lecturer[0]

    def __gt__(self, other):
        return self.average_grade_lecturer[0] > other.average_grade_lecturer[0]

    def __ne__(self, other):
        return self.average_grade_lecturer[0] != other.average_grade_lecturer[0]

    def __le__(self, other):
        return self.average_grade_lecturer[0] <= other.average_grade_lecturer[0]

    def __ge__(self, other):
        return self.average_grade_lecturer[0] >= other.average_grade_lecturer[0]

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # функция rate_hw() - это функция оценки студентов ревьюерами.
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')

# average_all_students(list_student, course) - функция подсчета средней оценки по всем студентам в рамках одного курса
def average_all_students(list_student, course):
    all_grades = []
    for student in list_student:
        for courses in list(student.grades.keys()):
            if course == courses:
                all_grades += student.grades[course]
    if len(all_grades) > 0:
        average_grade = sum(all_grades) / len(all_grades)
    else:
        average_grade = 0
    return average_grade

# average_all_lecturers(list_lecturer, course) - функция подсчета средней оценки по всем лекторам в рамках одного курса
def average_all_lecturers(list_lecturer, course):
    all_grades = []
    for lecturer in list_lecturer:
        for courses in list(lecturer.lecturer_grades.keys()):
            if course == courses:
                all_grades += lecturer.lecturer_grades[course]
    if len(all_grades) > 0:
        average_grade = sum(all_grades) / len(all_grades)
    else:
        average_grade = 0
    return average_grade


some_lecturer1 = Lecturer('lecturer1', 'LECTURER1') # создание класса some_lecturer1
some_lecturer1.courses_attached += ['Python'] # добавление курса Python в список предметов лектора1
some_lecturer2 = Lecturer('lecturer2', 'LECTURER2') # создание класса some_lecturer2
some_lecturer2.courses_attached += ['Python'] # добавление курса Python в список предметов лектора2

some_reviewer1 = Reviewer('reviewer1', 'REWIEWER1') # создание класса some_reviewer1
some_reviewer1.courses_attached += ['Python', 'Git'] # добавление курса Python и Git в список предметов рецензента1
some_reviewer2 = Reviewer('reviewer2', 'REWIEWER2') # создание класса some_reviewer2
some_reviewer2.courses_attached += ['Python', 'Git'] # добавление курса Python и Git в список предметов рецензента2

some_student1 = Student('student1', 'STUDENT1', 'mail') # создание класса some_student1
some_student1.courses_in_progress += ['Python', 'Git'] # добавление курса Python и Git в список предметов студента1
some_student1.finished_courses += ['Введение в программирование'] # добавление курса "Введение в программирование" в список оконченных предметов студента1
some_student1.rate_lec(some_lecturer1, 'Python', 9) # добавление оценки лектору1 студентом1 по курсу Python.
some_student1.rate_lec(some_lecturer2, 'Python', 3) # добавление оценки лектору2 студентом1 по курсу Python.
some_reviewer1.rate_hw(some_student1, 'Python', 5) # добавление оценки студенту1 рцензентом1 по курсу Python
some_reviewer1.rate_hw(some_student1, 'Git', 7) # добавление оценки студенту1 рцензентом1 по курсу Git
some_reviewer2.rate_hw(some_student1, 'Python', 9) # добавление оценки студенту1 рцензентом2 по курсу Python
some_reviewer2.rate_hw(some_student1, 'Git', 2) # добавление оценки студенту1 рцензентом2 по курсу Git

some_student2 = Student('student2', 'STUDENT2', 'mail') # создание класса some_student2
some_student2.courses_in_progress += ['Python', 'Git'] # добавление курса Python и Git в список предметов студента2
some_student2.finished_courses += ['Введение в программирование'] # добавление курса "Введение в программирование" в список оконченных предметов студента2
some_student2.rate_lec(some_lecturer1, 'Python', 5) # добавление оценки лектору1 студентом2 по курсу Python.
some_student2.rate_lec(some_lecturer2, 'Python', 10) # добавление оценки лектору2 студентом2 по курсу Python.
some_reviewer1.rate_hw(some_student2, 'Python', 8) # добавление оценки студенту2 рцензентом1 по курсу Python
some_reviewer1.rate_hw(some_student2, 'Git', 4) # добавление оценки студенту2 рцензентом1 по курсу Git
some_reviewer2.rate_hw(some_student1, 'Python', 4) # добавление оценки студенту2 рцензентом2 по курсу Python
some_reviewer2.rate_hw(some_student1, 'Git', 7) # добавление оценки студенту2 рцензентом2 по курсу Git

some_lecturer1.average_grade_lecturer[0] = average_lecturer(some_lecturer1.lecturer_grades) #подсчет с помощью функции average_lecturer(LecturerGrades)
                                                                                            # и передача среднего значения оценки в класс some_lecturer1(лектор1)
some_lecturer2.average_grade_lecturer[0] = average_lecturer(some_lecturer2.lecturer_grades)#подсчет с помощью функции average_lecturer(LecturerGrades)
                                                                                           # и передача среднего значения оценки в класс some_lecturer2(лектор2)
some_student1.average_grade_student[0] = average_student(some_student1.grades) #подсчет с помощью функции average_student(StudentGrades)
                                                                               # и передача среднего значения оценки в класс some_student1(студент1)
some_student2.average_grade_student[0] = average_student(some_student2.grades) #подсчет с помощью функции average_student(StudentGrades)
                                                                               # и передача среднего значения оценки в класс some_student2(студент2)

Students = [some_student1, some_student2] # список студентов для подсчета средней оценки в рамках одного курса
Lecturers = [some_lecturer1, some_lecturer2] # список лекторов для подсчета средней оценки в рамках одного курса

print(f'Рецензент1: \n'
      f'{some_reviewer1}')
print(f'Рецензент2: \n'
      f'{some_reviewer2}')
print(f'Лектор1: \n'
      f'{some_lecturer1}')
print(f'Лектор2: \n'
      f'{some_lecturer2}')
print(f'Студент1: \n'
      f'{some_student1}')
print(f'Студент2: \n'
      f'{some_student2}\n')

print('Сравнение средних оценок лектора1 и лектора2')
print(f'Средняя оценка лектора1 = Средняя оценка лектора2: {some_lecturer1 == some_lecturer2}')
print(f'Средняя оценка лектора1 < Средняя оценка лектора2: {some_lecturer1 < some_lecturer2}')
print(f'Средняя оценка лектора1 > Средняя оценка лектора2: {some_lecturer1 > some_lecturer2}')
print(f'Средняя оценка лектора1 != Средняя оценка лектора2: {some_lecturer1 != some_lecturer2}')
print(f'Средняя оценка лектора1 >= Средняя оценка лектора2: {some_lecturer1 >= some_lecturer2}')
print(f'Средняя оценка лектора1 <= Средняя оценка лектора2: {some_lecturer1 <= some_lecturer2}\n')

print('Сравнение средних оценок студента1 и студента2')
print(f'Средняя оценка студента1 = Средняя оценка студента2: {some_student1 == some_student2}')
print(f'Средняя оценка студента1 < Средняя оценка студента2: {some_student1 < some_student2}')
print(f'Средняя оценка студента1 > Средняя оценка студента2: {some_student1 > some_student2}')
print(f'Средняя оценка студента1 != Средняя оценка студента2: {some_student1 != some_student2}')
print(f'Средняя оценка студента1 >= Средняя оценка студента2: {some_student1 >= some_student2}')
print(f'Средняя оценка студента1 <= Средняя оценка студента2: {some_student1 <= some_student2}\n')

print(f'Средняя оценка всех студентов по курсу Python: {average_all_students(Students, 'Python')}')
print(f'Средняя оценка всех студентов по курсу Git: {average_all_students(Students, 'Git')}')
print(f'Средняя оценка всех лекторов по курсу Python: {average_all_lecturers(Lecturers, 'Python')}')
