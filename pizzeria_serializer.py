# Mateush Vilen Serializer lesson

import sqlite3


class PizzaDatabaseMixin:
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
    def create_table_pizza():
        conn = sqlite3.connect("Pizzeria_serializer.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE PIZZA ( ID INTEGER PRIMARY KEY, NAME VARCHAR(50) NOT NULL, PRICE DECIMAL(5,2) NOT NULL );")
        conn.commit()
        cursor.execute("INSERT INTO pizza VALUES (1, 'Blood pizza', 123.25);")
        conn.commit()
        cursor.execute("INSERT INTO pizza VALUES (2, 'Homeless pizza', 1.01);")
        conn.commit()
        cursor.execute("INSERT INTO pizza VALUES (3, 'Pizza with people skin', 250.00);")
        conn.commit()
        cursor.execute("INSERT INTO pizza VALUES (4, 'Pizza for unicorns', 980.00);")
        conn.commit()
        conn.close()

    @staticmethod
    def create_table_user():
        conn = sqlite3.connect("Pizzeria_serializer.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE USER ( ID INTEGER PRIMARY KEY, NAME VARCHAR(50) NOT NULL, ADRESS VARCHAR(50) );")
        conn.commit()
        cursor.execute("INSERT INTO user VALUES (1, 'Michael Jackson', 'sky');")
        conn.commit()
        cursor.execute("INSERT INTO user VALUES (2, 'John Travolta', 'Holywood');")
        conn.commit()
        cursor.execute("INSERT INTO user VALUES (3, 'Son of my mother friend', 'Best house in the world');")
        conn.commit()
        cursor.execute("INSERT INTO user VALUES (4, 'Cockroach of my head', 'My head');")
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
    def get_pizza_from_database():
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
    def get_user_from_database():
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


class Pizza(PizzaDatabaseMixin):
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


class User(PizzaDatabaseMixin):
    id = None
    name = ''
    adress = ''

    def __init__(self, id, name, adress):
        self.id = id
        self.name = name
        self.adress = adress

    def __getattr__(self, attr):
        return self.adress()

    @property
    def bill_text(self):
        return '{} {}'.format(self.name, self.adress)

    def __str__(self):
        return 'User: {}'.format(self.name)

    @staticmethod
    def get_fields():
        return ['id', 'name', 'adress']

class Order(PizzaDatabaseMixin):
    id = None
    name = ''
    adress = ''

    def __init__(self, id, name, adress):
        self.id = id
        self.name = name
        self.adress = adress


# Pizza.create_table_pizza()
# User.create_table_user()
# Order.create_table_order()
print('Users of my database:')
users = User.get_user_from_database()
for user in users:
    print(user.name, ', adress for order:', user.adress)
print('---------------------')
print('Pizzas is enabled for order:')
pizzas = Pizza.get_pizza_from_database()
for pizza in pizzas:
    # updated_name = pizza.name + " UPDATED"
    # pizza.update_pizza_name(updated_name)
    print(pizza.name, ', price:', pizza.price)
