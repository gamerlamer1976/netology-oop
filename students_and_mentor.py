class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            return None
        else:
            return 'Ошибка'

    def _get_average_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self._get_average_grade()}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._get_average_grade() < other._get_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._get_average_grade() == other._get_average_grade()


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

    def _get_average_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self._get_average_grade()}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._get_average_grade() < other._get_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._get_average_grade() == other._get_average_grade()


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

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


# =========================================================
# Аналитические функции (Задание 4)
# =========================================================

def calc_students_avg_grade(students_list, course):
    """Считает среднюю оценку за ДЗ по всем студентам в рамках курса."""
    total_sum = 0
    total_count = 0
    for student in students_list:
        if course in student.grades:
            total_sum += sum(student.grades[course])
            total_count += len(student.grades[course])
    if total_count == 0:
        return 0
    return round(total_sum / total_count, 1)


def calc_lecturers_avg_grade(lecturers_list, course):
    """Считает среднюю оценку за лекции всех лекторов в рамках курса."""
    total_sum = 0
    total_count = 0
    for lecturer in lecturers_list:
        if course in lecturer.grades:
            total_sum += sum(lecturer.grades[course])
            total_count += len(lecturer.grades[course])
    if total_count == 0:
        return 0
    return round(total_sum / total_count, 1)


# =========================================================
# ПОЛЕВЫЕ ИСПЫТАНИЯ
# =========================================================
if __name__ == '__main__':
    # 1. Создаем по 2 экземпляра каждого класса
    student_1 = Student('Ruoy', 'Eman', 'М')
    student_1.courses_in_progress += ['Python', 'Git']
    student_1.finished_courses += ['Введение в программирование']

    student_2 = Student('Ольга', 'Алёхина', 'Ж')
    student_2.courses_in_progress += ['Python', 'Java']
    student_2.finished_courses += ['Основы логики']

    lecturer_1 = Lecturer('Some', 'Buddy')
    lecturer_1.courses_attached += ['Python', 'Git']

    lecturer_2 = Lecturer('Иван', 'Иванов')
    lecturer_2.courses_attached += ['Python', 'Java']

    reviewer_1 = Reviewer('Пётр', 'Петров')
    reviewer_1.courses_attached += ['Python', 'Git']

    reviewer_2 = Reviewer('Анна', 'Смирнова')
    reviewer_2.courses_attached += ['Python', 'Java']

    # 2. Вызываем все методы
    # Эксперты ставят оценки студентам
    reviewer_1.rate_hw(student_1, 'Python', 10)
    reviewer_1.rate_hw(student_1, 'Git', 9)
    reviewer_1.rate_hw(student_2, 'Python', 8)

    reviewer_2.rate_hw(student_2, 'Java', 10)
    reviewer_2.rate_hw(student_2, 'Python', 9)

    # Студенты ставят оценки лекторам
    student_1.rate_lecture(lecturer_1, 'Python', 10)
    student_1.rate_lecture(lecturer_1, 'Git', 10)

    student_2.rate_lecture(lecturer_2, 'Python', 8)
    student_2.rate_lecture(lecturer_2, 'Java', 7)
    student_2.rate_lecture(lecturer_1, 'Python', 9)

    # Тестируем перегруженный __str__
    print("--- РЕВЬЮЕРЫ ---")
    print(reviewer_1)
    print()
    print(reviewer_2)
    print("\n--- ЛЕКТОРЫ ---")
    print(lecturer_1)
    print()
    print(lecturer_2)
    print("\n--- СТУДЕНТЫ ---")
    print(student_1)
    print()
    print(student_2)

    # Тестируем магические методы сравнения
    print("\n--- СРАВНЕНИЕ ---")
    print(f"Студент 1 круче Студента 2? {student_1 > student_2}")
    print(f"Лектор 1 хуже Лектора 2? {lecturer_1 < lecturer_2}")

    # 3. Тестируем глобальные функции
    print("\n--- ГЛОБАЛЬНАЯ АНАЛИТИКА ---")

    # Переименовываем переменные, чтобы не затенять аргументы функций
    all_students = [student_1, student_2]
    all_lecturers = [lecturer_1, lecturer_2]

    print(f"Средняя оценка студентов по курсу 'Python': {calc_students_avg_grade(all_students, 'Python')}")
    print(f"Средняя оценка лекторов по курсу 'Python': {calc_lecturers_avg_grade(all_lecturers, 'Python')}")