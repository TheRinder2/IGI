import math
from abc import ABC, abstractmethod


class Tree:
    def __init__(self, name: str, count: int, countOfNorm: int):
        self.name = name
        self.count = count
        self.countOfNorm = countOfNorm

    @classmethod
    def input(cls, message: str):
        print(message)
        try:
            name = input("\tname: ")
            count = int(input("\tcount: "))
            countOfNorm = int(input("\tcountOfNorm: "))
        except ValueError as err:
            print(f'Incorrect value: {err}')
        else:
            return Tree(name, count, countOfNorm)
    
    def __str__(self):
        return f'Tree(name: {self.name}\tcount: {self.count}\tcountOfNorm: {self.countOfNorm})'
    
    def __repr__(self):
        return f'Tree({self.name}, {self.count}, {self.countOfNorm})'
    

class Figure(ABC):
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = Color(color)

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def get_vertexes(self, x0: float, y0: float):
        pass


class Color:
    def __init__(self, color: str):
        self.hidden_color = color

    @property
    def color(self):
        return self.hidden_color

    @color.setter
    def color(self, color: str):
        self.hidden_color = color

    def __str__(self):
        return self.hidden_color


class IsoscelesRhomb(Figure):
    def __init__(self, name: str, color: str, a: float, r: float):
        super().__init__(name, color)
        self.a = a
        self.r = r

    def square(self):
        '''Returns square of trapezoid.'''

        return 2 * self.a * self.a * math.sin(math.radians(self.r)) * math.cos(math.radians(self.r))

    def __str__(self):
        return 'a: {}, r: {}, S: {}, color: {}'.format(self.a, self.r, self.square(), self.color)

    def get_vertexes(self, x0: float, y0: float) -> list:
        '''Returns set of points - vertexes of rhomb.'''

        a_cos = self.a * math.cos(math.radians(self.r))
        a_sin = self.a * math.sin(math.radians(self.r))
        return [[x0, y0], [a_cos, a_sin], [a_cos * 2, y0], [a_cos, -a_sin]]