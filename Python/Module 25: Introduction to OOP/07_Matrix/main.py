# TODO здесь писать код
class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        # Инициализируем матрицу нулями по заданным размерам
        self.data = [[0] * columns for _ in range(rows)]

    def __str__(self):
        # Метод должен возвращать строковое представление матрицы.
        # Выведите элементы строк через пробел, а сами строки — с новой строки.
        result = []
        for row in self.data:
            result.append(" ".join(str(element) for element in row))
        return '\n'.join(result)

    def set_data(self, values):
        # Метод принимает список списков и заполняет им self.data.
        if len(values) != self.rows or len(values[0]) != self.columns:
            raise ValueError ("Не корректные размеры!")
        self.data = values

    def add(self, other):
        # Метод сложения матриц
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Матрицы должны иметь одинаковые размеры!")

        result = Matrix(self.rows, self.columns)

        for add_row in range(self.rows):
            for add_column in range(self.columns):
                result.data[add_row][add_column] = self.data[add_row][add_column] + other.data[add_row][add_column]

        return result

    def subtract(self, other):
        # Метод вычитания матриц
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Матрицы должны иметь одинаковый размер!")

        result = Matrix(self.rows, self.columns)

        for subtract_row in range(self.rows):
            for subtract_column in range(self.columns):
                result.data[subtract_row][subtract_column] = self.data[subtract_row][subtract_column] - other.data[subtract_row][subtract_column]

        return result
    

    def multiply(self, other):
        # Метод умножения матриц
        if self.columns != other.rows:
            raise ValueError("Количество колонок первой матрицы должны быть равны количество строк второй матрицы!")

        result = Matrix(self.rows, other.columns)

        for multiply_row in range(self.rows):
            for multiply_column in range(other.columns):
                total = 0
                for multiply_element in range(self.columns):
                    total += self.data[multiply_row][multiply_element] * other.data[multiply_element][multiply_column]
                result.data[multiply_row][multiply_column] = total

        return result
    

    def transpose(self):
        # Метод транспонирования матрицы
        result = Matrix(self.columns, self.rows)

        for transpose_row in range(self.rows):
            for transpose_column in range(self.columns):
                result.data[transpose_column][transpose_row] = self.data[transpose_row][transpose_column]

        return result


# Примеры работы с классом:

# Создание экземпляров класса Matrix и заполнение данными
m1 = Matrix(2, 3)
m1.set_data([[1, 2, 3], [4, 5, 6]])

m2 = Matrix(2, 3)
m2.set_data([[7, 8, 9], [10, 11, 12]])

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.set_data([[1, 2], [3, 4], [5, 6]])

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())
