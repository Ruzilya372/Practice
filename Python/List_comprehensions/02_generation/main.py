long_catalog = int(input("Введите длину списка: "))
catalog = [1 if symbol % 2 == 0
           else (symbol % 5)
           for symbol in range(long_catalog)]

print("Результат: ", catalog)
