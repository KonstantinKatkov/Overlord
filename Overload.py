# Создайте новый класс Buiding
# Создайте инициализатор для класса Buiding, который будет задавать целочисленный атрибут
# этажности self.numberOfFloors и строковый атрибут self.buildingType
# Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
# Полученный код напишите в ответ к домашему заданию

class Buiding:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType



h1 = Buiding(10, "Десятиэтажный дом")
h2 = Buiding(10, "Десятиэтажный дом")

b1 = Buiding(5, "Пятиэтажный дом")
b2 = Buiding(3, "Трехэтажный дом")

print("Сравнение домов h1 и h2")
print(h1 == h2)
print()

print("Сравнение домов b1 и b2")
print(b1 == b2)