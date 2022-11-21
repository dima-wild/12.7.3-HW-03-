# Задание 16.9.4                      формирование списка приглашенных на корпоратив: через словарь

Customers = [{'firstname': 'Иван', 'lastname': 'Иванов', 'city': 'Москва', 'balance': 100},
             {'firstname': 'Петр', 'lastname': 'Петров', 'city': 'Москва', 'balance': 150},
             {'firstname': 'Федор', 'lastname': 'Федотов', 'city': 'Москва', 'balance': 170},
             {'firstname': 'Александр', 'lastname': 'Александров', 'city': 'Москва', 'balance': 130},
             {'firstname': 'Владимир', 'lastname': 'Владимиров', 'city': 'Москва', 'balance': 130}]

class Clients:
    def __init__(self, firstname = '', lastname = '', city = '', balance = 0):
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.balance = balance

    def get_guest(self, customer_from_dict):
        self.firstname = customer_from_dict.get('firstname')
        self.lastname = customer_from_dict.get('lastname')
        self.city = customer_from_dict.get('city')
        return f'{self.firstname} {self.lastname}, г.{self.city}'


print('Список приглашенных на корпоратив:')
for customer in Customers:
    customer_obj = Clients()
    customer_obj.get_guest(customer)
    print(customer_obj.get_guest(customer))
