#Задание №3

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
        self.average_grade_student = [0] # переменная для передачи в класс средней оценки студентов из функции average_student(StudentGrades)

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


