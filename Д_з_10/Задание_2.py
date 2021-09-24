#Задание №2

print('Добро пожаловать в ателье "Funny buttons"!\n '
      'Мы можем изготовить для Вас пальто и костюм.')
import math
from abc import ABC, abstractmethod

class AbsractOdezda(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def material(self):
        pass

class Odezda(AbsractOdezda):

    def __init__(self):
        pass

    @property
    def tkan_vsego(self):
        tkan = math.fsum([raschet_palto.material(), raschet_costum.material()])
        return str(f'Всего потребуется {tkan :.2f} метра ткани')

    def material(self):
        pass


class Palto(Odezda):
    def __init__(self, razmer):
        self.razmer = razmer
        super().__init__()

    def material(self):
        return self.razmer / 6.5 + 0.5


class Costum(Odezda):
    def __init__(self, rost):
        self.rost = rost
        super().__init__()

    def material(self):
        return self.rost / 100 * 2 + 0.3

while True:
    try:
        get_razmer = float(input('Введите размер (США - от 0 до 30): '))
        break
    except ValueError:
        print('Введите размер числом!')
while True:
    try:
        get_rost = float(input('Введите рост в сантиметрах: '))
        break
    except ValueError:
        print('Введите размер числом!')

raschet_palto = Palto(get_razmer)
raschet_costum = Costum(get_rost)
cosa = Odezda()
print(f'На пальто требуется {raschet_palto.material():.2f} метра ткани')
print(f'На костюм требуется {raschet_costum.material():.2f} метра ткани')
print(cosa.tkan_vsego)
print('Благодарим за выбор нашего ателье!')