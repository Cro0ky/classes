class Recipe:
    def __init__(self, name, ingradients):
        self.name = name
        self.ingradients = ingradients

    def print_ingradients(self):
        print(f"Инградиенты для {self.name}")
        for i in self.ingradients:
            print(f'- {i}')

    def cook(self):
        print(f'Сегодня мы готовим {self.name}\n'
              f'Выполняем инструкцию по приготовлению блюда {self.name}...\n'
              f'Блюдо {self.name} готово!')


bludo = Recipe('Спагетти болоньезе', ["Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
bludo.print_ingradients()
bludo.cook()