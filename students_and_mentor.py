class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    """Базовый класс преподавателей. Содержит только общие атрибуты."""

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Класс лекторов. Пока не имеет специфичных атрибутов или методов."""
    pass


class Reviewer(Mentor):
    """Класс экспертов. Отвечает за проверку домашних заданий."""

    def rate_hw(self, student, course, grade):
        """Метод выставления оценки студенту перенесен из базового класса Mentor."""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            return 'Успешно'
        else:
            return 'Ошибка'


# =========================================
# Исходный код тестирования (адаптированный)
# =========================================
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

# Вместо Mentor теперь создается экземпляр Reviewer,
# так как только он имеет право выставлять оценки
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(f"Оценки студента {best_student.name}: {best_student.grades}")

# =========================================
# Блок проверки из Задания №1
# =========================================
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')

print(isinstance(lecturer, Mentor))  # Ожидаемый вывод: True
print(isinstance(reviewer, Mentor))  # Ожидаемый вывод: True
print(lecturer.courses_attached)  # Ожидаемый вывод: []
print(reviewer.courses_attached)  # Ожидаемый вывод: []