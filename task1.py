#Задание №1
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# создание класса Lecturer на основе класса Mentor
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

# создание класса Reviewer на основе класса Mentor
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)






