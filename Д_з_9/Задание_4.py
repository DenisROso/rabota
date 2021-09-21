#Задание №4

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        return f'{self.name} едет.'

    def stop(self):
        return f'{self.name} остановилась.'

    def turn_left(self):
        return f'{self.name} поворачивает влево.'

    def turn_right(self):
        return f'{self.name} поворачивает вправо.'

    def show_speed(self):
        return f'\nВы двигаетесь со скоростью {self.speed} км/ч.'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВнимание! Вы превысили рекомендемую скорость {self.speed} км/ч.'
        else:
            return f'\nВы двигаетесь с допустимой скоростью {self.speed} км/ч.'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВнимание! Вы превысили рекомендемую скорость {self.speed}км/ч'
        else:
            return f'\nВы двигаетесь с допустимой скоростью {self.speed}км/ч'


class PoliceCar(Car):
    pass


town = TownCar(65, 'white', 'Lada-Kalina', 'False')
print('1:\n' + town.go(), town.show_speed(), town.turn_left(), town.turn_right(), town.stop())
sport = SportCar(200, 'Red', 'Ferrary', 'False')
print('2:\n' + sport.go(), sport.show_speed(), sport.turn_left(), sport.turn_right(), sport.stop())
work = WorkCar(35, 'gray', 'Gazelle', 'False')
print('3:\n' + work.go(), work.show_speed(), work.turn_left(), work.turn_right(), work.stop())
police = PoliceCar(90, 'green', 'UAZ-buhanka', 'True')
print('4:\n' + police.go(), police.show_speed(), police.turn_left(), police.turn_right(), police.stop())