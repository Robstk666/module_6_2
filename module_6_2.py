class Vehicle:
    # Атрибут класса - допустимые цвета
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        # Атрибуты объекта, с частично скрытыми свойствами
        self.owner = owner  # Владелец может меняться
        self.__model = model  # Название модели скрыто, менять нельзя
        self.__color = color  # Цвет скрыт, менять можно только через метод set_color
        self.__engine_power = engine_power  # Мощность скрыта, менять нельзя

    # Метод для получения модели транспорта
    def get_model(self):
        return f"Модель: {self.__model}"

    # Метод для получения мощности двигателя
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    # Метод для получения цвета транспорта
    def get_color(self):
        return f"Цвет: {self.__color}"

    # Метод для печати полной информации о транспорте
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    # Метод для изменения цвета
    def set_color(self, new_color):
        # Проверка, есть ли новый цвет в списке доступных цветов (регистр не учитывается)
        if new_color.lower() in map(str.lower, self.__COLOR_VARIANTS):
            self.__color = new_color.capitalize()
        else:
            print(f"Нельзя сменить цвет на {new_color}")


# Класс Sedan, наследующий класс Vehicle
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # Ограничение на количество пассажиров

    def __init__(self, owner, model, color, engine_power):
        # Инициализация родительского класса Vehicle
        super().__init__(owner, model, color, engine_power)


# Проверка работы кода
if __name__ == "__main__":
    # Создаем объект класса Sedan с заданными параметрами
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
    vehicle1.print_info()

    # Попробуем поменять цвет и владельца
    vehicle1.set_color('Pink')  # Недопустимый цвет
    vehicle1.set_color('BLACK')  # Допустимый цвет
    vehicle1.owner = 'Vasyok'    # Меняем владельца

    # Проверяем изменения
    vehicle1.print_info()