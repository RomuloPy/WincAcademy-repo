# Object Orientated Programming in Python

# class Dog:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_name(self):
#         return self.name

#     def get_age(self):
#         return self.age


# piloto = Dog("Piloto", 7)
# gorby = Dog("Gorby", 5)
# backy = Dog("Backy", 4)
# rex = Dog("Rex", 2)

# print(piloto.get_name(), piloto.get_age())
# print(gorby.name, gorby.get_age())

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade  # 0 - 100

#     def get_grade(self):
#         return self.grade


# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []

#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False

#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
        
#         return value / len(self.students)


# student1 = Student('Rómulo', 44, 85)
# student2 = Student('Rafael', 20, 80)
# student3 = Student('Jason', 10, 80.5)

# course = Course("Math", 2)
# course.add_student(student1)
# course.add_student(student2)
# print(course.students[0].name)
# print(course.get_average_grade())
# #
# #
# #
# # Inheritance


# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(f'I am {self.name} and I am {self.age} years old')

#     def speak(self):
#         print('I cannot speak...')


# class Cat(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color

#     def speak(self):
#         print('Meow')

#     def show(self):
#         print(f'I am {self.name} and I am {self.age} years old and I am {self.color}')

# class Dog(Pet):
#     def speak(self):
#         print('Bark')


# class Fish(Pet):
#     pass


# p = Pet("Piloto", 7)
# p.show()
# c = Cat("Bigodes", 3, "Grey")
# c.show()
# c.speak()
# d = Dog("Backy", 12)
# d.show()
# d.speak()
# f = Pet("Nemo", 1)
# f.show()
# f.speak()

# Tests with Pytest
# def test_example_0():
#     assert 1 == 1


# def test_example_1():
#     assert 1 == 2

# def initials(name):
#     first, last = name.split(' ')
#     f, l = first[0], last[0]
#     return f'{f}. {l}.'

# def test_initials_common_name():
#     assert initials('Daniel Radcliffe') == 'D. R.'

# def test_intials_double_barrelled():
#     assert initials('Helena Bonham Carter') == 'H. B. C.'


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
    

dev1 = Employee('Rómulo', 'Santos', 50000)
print(dev1.email)