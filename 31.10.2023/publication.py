class Publication:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        print(f'Название - {self.title}')
        print(f'Автор - {self.author}')
        print(f'Год издания - {self.year}')


class Book(Publication):

    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self.isbn = isbn

    def display(self):
        super().display()
        print(f'isbn - {self.isbn}')


class Magazine(Publication):

    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def display(self):
        super().display()
        print(f'Номер выпуска - {self.issue_number}')


# p = Publication('Title', 'Author', 2023)
# p.display()
# b = Book('Title2', 'Author1', 1998, 123245213)
# b.display()

n = Magazine('Title3', 'Author3', 1975, 2)
n.display()
