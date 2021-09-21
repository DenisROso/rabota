#Задание №1

import time


def decor(func):
    def wrapper(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        print(f'Ожидание составило: {end_time - start_time} сек.')

    return wrapper


class TrafficLight:
    __color = 'red'
    __cl_data = {'red': (7, 'yellow', 'Красный'), 'yellow': (), 'green': (4, 'yellow', 'Зеленый')}
    __direct_el = (2, 'green', 'Желтый')
    __reverse_el = (2, 'red', 'Желтый')

    @decor
    def running(self, new_color):
        if self.__color == 'red':
            self.__cl_data['yellow'] = self.__direct_el
        elif self.__color == 'green':
            self.__cl_data['yellow'] = self.__reverse_el

        print(f'Сейчас светофор: {self.__cl_data[self.__color][2]}')
        if new_color == self.__cl_data[self.__color][1]:
            ticker = self.__cl_data[self.__color][0]
            while ticker > 0:
                print(ticker)
                ticker = ticker - 1
                time.sleep(1)
            self.__color = new_color
            print(f'Цвет светофора сменился на: {self.__cl_data[self.__color][2]}')
        else:
            raise Exception('Неверное значение цвета!')

    def current_l(self):
        return self.__cl_data[self.__color]
    def next_color(self):
        self.running(self.__cl_data[self.__color][1])


l1 = TrafficLight()
l1.running('yellow')
print(f'Текущий цвет: {l1.current_l()[2]}')
l1.next_color()  # Зеленый
l1.next_color()  # Желтый.
l1.next_color()  # Красный.