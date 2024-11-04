class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # Название здания
        self.number_of_floors = number_of_floors  # Количество этажей

    def __len__(self):
        return self.number_of_floors  # Возвращаем количество этажей

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"  # Форматируем строку для вывода

# Пример выполнения кода
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)  # Вывод: Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Вывод: Название: ЖК Акация, кол-во этажей: 20

# __len__
print(len(h1))  # Вывод: 10
print(len(h2))  # Вывод: 20