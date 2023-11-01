class BankAccount:
    history = []

    def __init__(self, balance, int_rate, trans):
        self.__balance = balance
        self.__int_rate = int_rate
        self.__trans = trans

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print(f'Внесение наличных на счет {amount}')
        self.history.append('Внесение наличных')

    def withdraw(self, amount):
        self.__balance = self.__balance - amount
        print(f'Снятие наличных {amount}')
        self.history.append('Снятие наличных')

    def add_intrest(self):
        self.__balance = self.__balance * self.__int_rate / 100 + self.__balance
        print(f"Начиленны проценты по вкладу {self.__balance * self.__int_rate / 100}")
        self.history.append('Начисление процентов на счет')

    def history_list(self):
        print('\nИстория платежей:')
        for i in self.history:
            print(f'- {i}')


account = BankAccount(100000, 0.05, 1)
account.deposit(15000)
account.withdraw(7500)
account.add_intrest()
account.history_list()
