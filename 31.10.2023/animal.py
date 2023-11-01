class Animal:
    def __init__(self, name, spicies, legs):
        self.name = name
        self.spicies = spicies
        self.legs = legs

    def voice(self):
        print(f'{self.name} подает голос')

    def move(self):
        print(f'{self.name} дергает хвостом')


class Dog(Animal):
    def __init__(self, name, breed, legs):
        super().__init__(name=name, legs=legs, spices='dog')
        self.breed = breed

    def bark(self):
        print(f'{self.breed} {self.name} лает')


class Bird(Animal):
    def __init__(self, name, spices, wingman):
        super().__init__(name=name, spices=spices, legs=2)
        self.wingman = wingman

    def fly(self):
        print(f'{self.spicies} {self.name} летает')


dog = Dog("Геральт", "доберман", 4)
bird = Bird("Вася", "попугай", 2)
dog.voice()
bird.voice()
dog.move()
bird.move()
dog.bark()
bird.fly()
