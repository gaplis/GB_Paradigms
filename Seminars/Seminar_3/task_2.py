# Задание 2:
#
# Контекст:
# Теперь, когда у вас есть абстрактный класс Shape, ваша следующая задача - получить класс Circle.
#
# Задача:
# Реализовать дочерний от Shape класс Circle, включая следующие работающие методы:
# ○ конструктор класса __init__ - метод инициализации класса Circle.
# ○ get_area - метод для расчета площади круга
# ○ get_perimeter - метод для расчета периметра окружности

from task_1 import Shape
import math


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 2 * math.pi * self.radius

    def get_perimeter(self):
        return math.pi * self.radius ** 2