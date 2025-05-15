class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_hw = {}  # Оценки за ДЗ от Reviewer
        self.average_grade_hw = 0  # Добавляем инициализацию средней оценки

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if grade < 0 or grade > 10:
                return 'Ошибка: оценка должна быть от 0 до 10'
            if course in lecturer.grades_lecture:
                lecturer.grades_lecture[course].append(grade)
            else:
                lecturer.grades_lecture[course] = [grade]

            # Пересчет средней оценки лектора
            all_grades = []
            for grades in lecturer.grades_lecture.values():
                all_grades.extend(grades)
            if all_grades:
                lecturer.average_grade = sum(all_grades) / len(all_grades)
            else:
                lecturer.average_grade = 0
            return lecturer.average_grade
        else:
            return 'Ошибка'

    def average_hw_in_courses(self, student, course):
        hw_in_course = []
        if isinstance(student, Student) and course in student.courses_in_progress:
            for grades in student.grades_hw.values():
                hw_in_course.extend(grades)
            if hw_in_course:
                student.average_grade_hw_in_course = sum(hw_in_course) / len(hw_in_course)
            else:
                student.average_grade_hw_in_course = 0
            return student.average_grade_hw_in_course


    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Некорректный ввод'
        else:
            return self.average_grade_hw > other.average_grade_hw
    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Некорректный ввод'
        else:
            return self.average_grade_hw == other.average_grade_hw
    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Некорректный ввод'
        else:
            return self.average_grade_hw < other.average_grade_hw
    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашнее задание: {self.average_grade_hw}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecture = {}  # Оценки за лекции от студентов
        self.average_grade = 0  # Добавляем инициализацию средней оценки

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade}')
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Некорректный ввод'
        else:
            return self.average_grade > other.average_grade
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Некорректный ввод'
        else:
            return self.average_grade == other.average_grade
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Некорректный ввод'
        else:
            return self.average_grade < other.average_grade
    def average_in_courses(self, lecturer, course):
        a=[]
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            for grades in lecturer.grades_lecture.values():
                a.extend(grades)
            if a:
                lecturer.average_grade_in_course = sum(a) / len(a)
            else:
                lecturer.average_grade_in_course = 0
            return lecturer.average_grade_in_course



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if grade < 0 or grade > 10:
                return 'Ошибка: оценка должна быть от 0 до 10'
            if course in student.grades_hw:
                student.grades_hw[course].append(grade)
            else:
                student.grades_hw[course] = [grade]

            # Пересчет средней оценки студента
            all_grades = []
            for grades in student.grades_hw.values():
                all_grades.extend(grades)
            if all_grades:
                student.average_grade_hw = sum(all_grades) / len(all_grades)
            else:
                student.average_grade_hw = 0
        else:
            return 'Ошибка'


    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student1 = Student("Иван", "Иванов", "мужской")
student1.courses_in_progress = ["Python", "Git"]
student1.finished_courses = ["Введение в программирование"]

student2 = Student("Мария", "Петрова", "женский")
student2.courses_in_progress = ["Python", "Git", "SQL"]
student2.finished_courses = ["Основы программирования"]


lecturer1 = Lecturer("Алексей", "Смирнов")
lecturer1.courses_attached = ["Python", "Git"]

lecturer2 = Lecturer("Елена", "Кузнецова")
lecturer2.courses_attached = ["Python", "SQL"]


reviewer1 = Reviewer("Дмитрий", "Васильев")
reviewer1.courses_attached = ["Python", "Git"]

reviewer2 = Reviewer("Ольга", "Николаева")
reviewer2.courses_attached = ["SQL", "Git"]


print("--- Оценка домашних заданий ---")
reviewer1.rate_hw(student1, "Python", 9)
reviewer1.rate_hw(student1, "Python", 8)
reviewer1.rate_hw(student1, "Git", 10)
reviewer1.rate_hw(student1, "Git", 7)

reviewer1.rate_hw(student2, "Python", 10)
reviewer1.rate_hw(student2, "Python", 9)
reviewer1.rate_hw(student2, "Git", 8)

reviewer2.rate_hw(student2, "Git", 9)
reviewer2.rate_hw(student2, "SQL", 10)


print("\n--- Оценка лекций ---")
student1.rate_lecture(lecturer1, "Python", 9)
student1.rate_lecture(lecturer1, "Git", 8)
student2.rate_lecture(lecturer1, "Python", 10)

student1.rate_lecture(lecturer2, "Python", 8)
student2.rate_lecture(lecturer2, "Python", 9)
student2.rate_lecture(lecturer2, "SQL", 10)


print("\n--- Информация о студентах ---")
print(student1)
print()
print(student2)

print("\n--- Информация о лекторах ---")
print(lecturer1)
print()
print(lecturer2)

print("\n--- Информация о проверяющих ---")
print(reviewer1)
print()
print(reviewer2)


print("\n--- Сравнение студентов ---")
print(f"Студент1 > Студент2: {student1 > student2}")
print(f"Студент1 == Студент2: {student1 == student2}")
print(f"Студент1 < Студент2: {student1 < student2}")

print("\n--- Сравнение лекторов ---")
print(f"Лектор1 > Лектор2: {lecturer1 > lecturer2}")
print(f"Лектор1 == Лектор2: {lecturer1 == lecturer2}")
print(f"Лектор1 < Лектор2: {lecturer1 < lecturer2}")


print("\n--- Добавление завершенных курсов ---")
student1.add_courses("Основы ООП")
student2.add_courses("Базы данных")


print("\n--- Средние оценки по курсам ---")
print("Средняя оценка лектора1 по Python:")
lecturer1.average_in_courses(lecturer1, "Python")

print("\nСредняя оценка лектора2 по Python:")
lecturer2.average_in_courses(lecturer2, "Python")

print("\n--- Средние оценки по курсам ---")
print("Средняя оценка лектора1 по Python:")
student1.average_hw_in_courses(student1, "Python")

print("\n--- Проверка на некорректный ввод ---")
print(student1 > lecturer1) # Сравнение студента с лектором
print(lecturer1 == student2) # Сравнение лектора со студентом

print("\n--- Проверка на некорректные оценки ---")
print(reviewer1.rate_hw(student1, "Python", 11)) # Оценка больше 10
print(student1.rate_lecture(lecturer1, "Python", -1)) # Оценка меньше 0

print("\n--- Проверка на несуществующие курсы ---")
print(reviewer1.rate_hw(student1, "C++", 8)) # Курс не прикреплен
print(student1.rate_lecture(lecturer1, "SQL", 9)) # Курс не прикреплен

