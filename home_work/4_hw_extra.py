class Car:
    def __init__(self, color=None, type=None, year=None):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        return 'Автомобиль заведен'

    def stop(self):
        return 'Автомобиль заглушен'

    def color_assign(self):
        return (f'Цвет автомобиля: {self.color}')

    def type_assign(self):
        return (f'Тип автомобиля: {self.type}')

    def year_assign(self):
        return (f'Год выпуска автомобиля: {self.year}')


car = Car('красный', 'седан', '2024')
print('Автомобиль: ' '\n', car.color_assign(), '\n', car.type_assign(), '\n', car.year_assign())
print(car.start())
print(car.stop())
