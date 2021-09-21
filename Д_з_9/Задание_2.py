#Задание №2

# Вариант 1
class Road:

        def __init__(self, length: [int, float], width: [int, float], height: [int, float], mass):
            self._length = float(length)
            self._width = float(width)
            self._height = float(height)
            self.__mass = mass


        def asfalt_mass(self):
            self.rezult = self._length * self._width * self._height * self.__mass / 1000
            print('Для дороги длиной', self._length, 'м, шириной', self._width, 'м и толщиной дорожного покрытия',
                  self._height, 'см потребуется:', self.rezult, 'т асфальта.')

mass = 25 #кг, вес покрытия одного кв метра дороги асфальтом, толщиной в 1 см
length = input('Введите длину дорожного полотна, м: ')
width = input('Введите ширину дорожного полотна, м: ')
height = input('Введите толщину дорожного покрытия, см: ')
mass_road = Road(length, width, height, mass)
mass_road.asfalt_mass()

# Вариант 2
class Road:

    _length = 0
    _width = 0
    __mass = 25 #кг
    __height = 5 #см

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def asfalt_mass(self):
        return self._length * self._width * self.__mass * self.__height /1000