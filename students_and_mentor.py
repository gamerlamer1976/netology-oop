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
        # Форматирование списков в строки через запятую
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        avg_grade = self._get_average_grade()

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade}\n"
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


# =========================================
# Блок проверки работоспособности Задания №3
# =========================================
if __name__ == '__main__':
    # Создание студентов
    student_1 = Student('Ruoy', 'Eman', 'М')
    student_1.courses_in_progress += ['Python', 'Git']
    student_1.finished_courses += ['Введение в программирование']

    student_2 = Student('Ольга', 'Алёхина', 'Ж')
    student_2.courses_in_progress += ['Python']

    # Создание лекторов и экспертов
    lecturer_1 = Lecturer('Some', 'Buddy')
    lecturer_1.courses_attached += ['Python', 'Git']

    lecturer_2 = Lecturer('Иван', 'Иванов')
    lecturer_2.courses_attached += ['Python']

    reviewer_1 = Reviewer('Пётр', 'Петров')
    reviewer_1.courses_attached += ['Python', 'Git']

    # Выставление оценок
    reviewer_1.rate_hw(student_1, 'Python', 10)
    reviewer_1.rate_hw(student_1, 'Git', 9)
    reviewer_1.rate_hw(student_2, 'Python', 8)

    student_1.rate_lecture(lecturer_1, 'Python', 10)
    student_1.rate_lecture(lecturer_1, 'Git', 10)
    student_2.rate_lecture(lecturer_2, 'Python', 7)

    # Проверка работы __str__
    print(reviewer_1)
    print("---")
    print(lecturer_1)
    print("---")
    print(student_1)
    print("---")

    # Проверка операторов сравнения
    print(f"Сравнение лекторов (lecturer_1 > lecturer_2): {lecturer_1 > lecturer_2}")  # Ожидается True (10.0 > 7.0)
    print(f"Сравнение студентов (student_1 < student_2): {student_1 < student_2}")  # Ожидается False (9.5 < 8.0)
    print(f"Равенство студентов (student_1 == student_2): {student_1 == student_2}")  # Ожидается False