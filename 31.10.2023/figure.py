class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

    def draw(self):
        return 'Рисуем фигуру'


class Line(Figure):
    def draw(self):
        return 'Рисуем линию'


class Rectangle(Figure):
    def __init__(self, coords, width, color, side):
        super().__init__(coords, width, color)
        self.side = side

    def draw(self):
        return 'Рисуем прямоугольник'

    def square(self):
        return f'Площадь равна - {self.side * self.side}'


class Ellipse(Figure):
    def draw(self):
        return 'Рисуем эллипс'


def try_to_draw(object):
    print(object.draw())

f = Figure([2, 2, 3, 4, 5, 5], 3, 'black')
print(f.coords)
print(f.draw())
f1 = Line([1, 2, 3, 4], 3, 'Purple')
print(f'{f1.draw()}: толщеной - {f1.width}, цветом - {f1.color}')
r = Rectangle([1, 1, 2, 3], 6, 'yellow', 4)
print(r.square())
try_to_draw(r)
