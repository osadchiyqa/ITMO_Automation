class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def perimetr(self):
        return self.width + self.height + self.width + self.height

calc = Rectangle(2, 3)

print(calc.square())
print(calc.perimetr())


class Triangle:
    def __init__(self, a, b, c, height):
        self.a = a
        self.b = b
        self.c = c
        self.height = height

    def square(self):
        return 0.5 * max(self.a, self.b, self.c) * self.height

    def perimetr(self):
        return self.a + self.b + self.c

calc = Triangle(2, 3, 6, 5)

print(calc.square())
print(calc.perimetr())


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14159


    def square(self):
        return self.pi * self.radius * self.radius

    def perimetr(self):
        return 2 * self.pi * self.radius

calc = Circle(3)

print(calc.square())
print(calc.perimetr())


class Math:
    def __init__(self, a, b,):
        self.a = a
        self.b = b

    def addition (self):
        return self.a + self.b

    def multiplication (self):
        return  self.a * self.b

    def division (self):
        return  self.a / self.b

    def subtraction (self):
        return self.a - self.b

count = Math(3, 2)

print(count.addition())
print(count.multiplication())
print(count.division())
print(count.subtraction())


class Button:
    def __init__(self, text):
        self.text = text
        self.type = 'Кнопка'
        self.loc = '      '

    def click(self):
        return f'Клик по кнопке {self.text}'

elements = [Button('Text Box'),
           Button('Check Box'),
           Button('Radio Button'),
           Button('Web Tables'),
           Button('Buttons'),
           Button('Links'),
           Button('Broken Links - Images'),
           Button('Upload and Download'),
           Button('Dynamic Properties')]

for button in elements:
    print(f"Кнопка: {button.text}, Тип: {button.type}, Локатор: '{button.loc}")
    print(button.click())
