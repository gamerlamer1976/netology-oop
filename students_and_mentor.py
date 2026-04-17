class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            # Опционально: можно добавить проверку, что grade находится в диапазоне 1-10
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            # Для избежания предупреждения "Missing return statement" в PyCharm,
            # можно явно вернуть None, хотя это происходит и автоматически.
            return None
        else:
            return 'Ошибка'


class Mentor:
    """Базовый класс преподавателей."""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Класс лекторов."""
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    """Класс экспертов."""
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            return 'Успешно'
        else:
            return 'Ошибка'


# =========================================
# Блок проверки из Задания №2
# =========================================
if __name__ == '__main__':
    # Переименовали переменные, чтобы они не затеняли аргументы методов
    cool_lecturer = Lecturer('Иван', 'Иванов')
    expert_reviewer = Reviewer('Пётр', 'Петров')
    best_student = Student('Алёхина', 'Ольга', 'Ж')

    best_student.courses_in_progress += ['Python', 'Java']
    cool_lecturer.courses_attached += ['Python', 'C++']
    expert_reviewer.courses_attached += ['Python', 'C++']

    # Вызовы методов с новыми именами переменных
    print(best_student.rate_lecture(cool_lecturer, 'Python', 7))  # Ожидаемый вывод: None
    print(best_student.rate_lecture(cool_lecturer, 'Java', 8))    # Ожидаемый вывод: Ошибка
    print(best_student.rate_lecture(cool_lecturer, 'C++', 8))     # Ожидаемый вывод: Ошибка
    print(best_student.rate_lecture(expert_reviewer, 'Python', 6))  # Ожидаемый вывод: Ошибка

    print(cool_lecturer.grades) # Ожидаемый вывод: {'Python': [7]}