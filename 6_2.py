class Vehicle:

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self, __model):
        if isinstance(str, __model):
            return f"Модель: {self.__model}"

    def get_horsepower(self, __engine_power):
        if isinstance(int, __engine_power):
            return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self, __color):
        if isinstance(__color, str):
            return f"Цвет: {self.__color}"

    def print_info(self):
        __model = self.get_model()
        horsepower = self.get_horsepower()
        __color = self.get_color()
        print(f"Модель: {model}\nМощность двигателя: {horsepower} лошадиных сил\nЦвет: {color}\nВладелец: {self.owner}")

    def set_color(self, new_color):
        if isinstance(new_color, str) and new_color in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    def __PASSENGERS_LIMIT(self, number):
        number = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
