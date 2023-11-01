class Student:
    def __init__(self, name, age, grade, scores):
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = scores

    def average_score(self):
        print(sum(self.scores) / len(self.scores))

    def display(self):
        print(f'Name: {self.name}\n'
              f'Age: {self.age}\n'
              f'Grade: {self.grade}\n'
              f'Scorse: {self.scores}')


student1 = Student('Name', 16, 10, [4, 4, 5, 5, 4])
student1.display()
student1.average_score()
