# Mateush Vilen Serializer lesson

import sqlite3


class PizzeriaDatabaseMixin:
    @staticmethod
    def __run_sql_command(command):
        conn = sqlite3.connect("Pizzeria_serializer.db")
        cursor = conn.cursor()
        cursor.execute(command)
        conn.close()

    def update_pizza_name(self, name):
        command = "UPDATE PIZZA SET NAME = '{0}' WHERE ID = {1};".format(name, self.id)
        Pizza.__run_sql_command(command)
        self.name = name

    @staticmethod
    def create_test_data_for_pizza():
        test_data = []
        test_data.append([1, 'Blood pizza', 123.25])
        test_data.append([2, 'Homeless pizza', 1.01])
        test_data.append([3, 'Pizza with people skin', 250.00])
        test_data.append([4, 'Pizza for unicorns', 980.00])
        conn = sqlite3.connect("Pizzeria_serializer.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE PIZZA ( ID INTEGER PRIMARY KEY, NAME VARCHAR(50) NOT NULL, PRICE DECIMAL(5,2) NOT NULL );")
        conn.commit()
        for test_write in test_data:
            cursor.execute("INSERT INTO pizza VALUES (?, ?, ?);", (test_write[0], test_write[1], test_write[2]))
            conn.commit()
        conn.close()
        test_data.clear()

    @staticmethod
    def create_test_data_for_user():
        test_data = []
        test_data.append([1, 'Michael Jackson', 'sky'])
        test_data.append([2, 'John Travolta', 'Hollywood'])
        test_data.append([3, 'Son of my mother friend', 'Best house in the world'])
        test_data.append([4, 'Cockroach of my head', 'My head'])
        conn = sqlite3.connect("Pizzeria_serializer.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE USER ( ID INTEGER PRIMARY KEY, NAME VARCHAR(50) NOT NULL, address VARCHAR(50) );")
        conn.commit()
        for test_write in test_data:
            cursor.execute("INSERT INTO user VALUES (?, ?, ?);", (test_write[0], test_write[1], test_write[2]))
            conn.commit()
        conn.close()

    @staticmethod
    def create_table_order():
        conn = sqlite3.connect("Pizzeria_serializer.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE ORDER ( ID INTEGER PRIMARY KEY, NAME_USER VARCHAR(50) NOT NULL, NAME_PIZZA VARCHAR(50) NOT NULL);")
        conn.commit()
        conn.close()

    @staticmethod
    def get_pizzas_from_database():
        conn = sqlite3.connect("Pizzeria_serializer.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pizza")
        raw_pizza = cursor.fetchall()
        conn.close()
        pizzas = []
        for raw in raw_pizza:
            pizza = Pizza(*raw)
            pizzas.append(pizza)
        return pizzas

    @staticmethod
    def get_users_from_database():
        conn = sqlite3.connect("Pizzeria_serializer.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user")
        raw_user = cursor.fetchall()
        conn.close()
        users = []
        for raw in raw_user:
            user = User(*raw)
            users.append(user)
        return users

    @staticmethod
    def create_table():
        pass

    @staticmethod
    def add_pizza_to_database():
        pass


class Pizza(PizzeriaDatabaseMixin):
    id = None
    name = ''
    price = 0.00

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __getattr__(self, attr):
        return self.name.upper()

    # @property
    # def full_name(self):
    #     return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return 'Pizza: {}'.format(self.name)

    @staticmethod
    def get_fields():
        return ['id', 'name', 'price']


class User(PizzeriaDatabaseMixin):
    id = None
    name = ''
    address = ''

    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    def __getattr__(self, attr):
        return self.address()

    @property
    def bill_text(self):
        return '{} {}'.format(self.name, self.address)

    def __str__(self):
        return 'User: {}'.format(self.name)

    @staticmethod
    def get_fields():
        return ['id', 'name', 'address']


class Order(PizzeriaDatabaseMixin):
    id = None
    name = ''
    address = ''

    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address


def main():
    Pizza.create_test_data_for_pizza()
    User.create_test_data_for_user()
    # Order.create_table_order()
    print('Users of my database:')
    users = User.get_users_from_database()
    for user in users:
        print(user.name, ', address for order:', user.address)
    print('---------------------')
    print('Pizzas is enabled for order:')
    pizzas = Pizza.get_pizzas_from_database()
    for pizza in pizzas:
        # updated_name = pizza.name + " UPDATED"
        # pizza.update_pizza_name(updated_name)
        print(pizza.name, ', price:', pizza.price)


if __name__ == '__main__':
    main()
