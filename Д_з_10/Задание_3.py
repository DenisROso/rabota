#Задание №3

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Клетки объединились. Теперь размер клетки равен: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Клетка уменьшилась. Теперь размер клетки равен: {sub}' if sub > 0 else 'Клетка уничтожена.'

    def __truediv__(self, other):
        return f'Клетка разделилась. Теперь размер клетки равен: {self.quantity // other.quantity}'

    def __mul__(self, other):
        return f'Клетки умножились. Теперь размер клетки равен: {self.quantity * other.quantity}'

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += f'{"*" * row} \n'
        result += f'{"*" * (self.quantity % row)}'
        return result


cell = Cell(15)
cell_2 = Cell(3)

print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(4))
