def get_params(a: str = None, b: str = None) -> None:
    while True:
        a = input('Введите длину прямоугольника ')
        b = input('Введите ширину прямоугольника ')
        try:
            a = float(a)
            b = float(b)
            break
        except ValueError as e:
            print(f'Ваш ввод првёл к ошибке ValueError: {e}\n'f'Попробуйте снова')
            break

    return a, b


class Rectangle:

    def __init__(self, side_a: float, side_b=None):
        self.side_a = side_a

        if side_b is None:
            self.side_b = side_a
        else:
            self.side_b = side_b

    def chek(self, a, b):
                if a < 0 or b < 0:
                    print("Введите положительные значения для стороны прямоугольника")
    def square_rectangle(self):
        return self.side_a * self.side_b
    def len_rectangle(self):
        return (self.side_a + self.side_b) * 2


get_params("Введите сторону")
a = float(input('Введите проверенную длину '))
b = float(input("Введите проверенную ширину "))
rect = Rectangle(a, b)
print(rect.len_rectangle(), rect.square_rectangle())