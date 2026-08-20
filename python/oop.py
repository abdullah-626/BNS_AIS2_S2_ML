# class StudentInfo:
#     name = "George"
#     age = 39

#     def std_info(self):
#         print(self)


# s1 = StudentInfo()
# print(s1)
# print(s1.std_info())

# class Student:

#     def __init__(self, name: str = "test", age: int = 20) -> None:
#         self.name = name
#         self.age = age
#         self.grade = 100

#     def get_info(self):
#         return f"my name is {self.name},my age s {self.age}"


from abc import ABC, abstractmethod


# class Animal(ABC):
#     @abstractmethod
#     def move(self):
#         pass


# class Bird(Animal):
#     pass


# a = Bird()
# a.move()


class Shape:
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side**2


x = Circle(5)
y = Rectangle(4, 6)
z = Triangle(3, 4)
w = Square(5)