import mysql.connector
from mysql.connector import Error


class Database:

    def __init__(self):
        try:
            self.sql = mysql.connector.connect(
                user='root', password='Root@2020', host='127.0.0.1', port='3306', database='foodplaza')
            self.mycursor = self.sql.cursor()
        except Error as er:
            print('='*30)
            print(er)
            print('='*30)


class CustomerDB(Database):

    def __init__(self):
        super().__init__()
        self.mycursor.execute('CREATE TABLE IF NOT EXISTS customers(customer_id int AUTO_INCREMENT, customer_name varchar(100), customer_email varchar(100) UNIQUE, customer_password varchar(50), customer_address varchar(200), customer_contact varchar(11), PRIMARY KEY(customer_id))')
        self.sql.commit()

    def show_all_customers(self):
        query = 'select customer_id, customer_name, customer_email, customer_address, customer_contact from customers'
        try:
            self.mycursor.execute(query)
            data = self.mycursor.fetchall()
            if data:
                return data
        except Error as er:
            print('='*30)
            print(er)
            print('='*30)
        finally:
            self.mycursor.close()
            self.sql.close()

    def add_customer(self, name=None, email=None, password=None, address=None, contact=None):
        query = 'insert into customers(customer_name, customer_email, customer_password, customer_address, customer_contact) values(%s,%s,md5(%s),%s,%s)'
        args = (name, email, password, address, contact)
        try:
            self.mycursor.execute(query, args)
            self.sql.commit()
            if self.mycursor.execute:
                return True
        except Error as er:
            print('='*30)
            print(er)
            print('='*30)
        finally:
            self.mycursor.close()
            self.sql.close()

    def update_customer(self, name=None, address=None, contact=None, email=None):
        query = 'update customers set customer_name=%s, customer_address=%s, customer_contact=%s where customer_email=%s'
        args = (name, address, contact, email)
        try:
            self.mycursor.execute(query, args)
            self.sql.commit()
            if self.mycursor.execute:
                return True
        except Error as er:
            print('='*30)
            print(er)
            print('='*30)
        finally:
            self.mycursor.close()
            self.sql.close()

    def delete_customer(self, email):
        query = 'delete from customers where customer_email=%s'
        args = (email,)
        try:
            self.mycursor.execute(query, args)
            self.sql.commit()
            if self.mycursor.execute:
                return True
        except Error as er:
            print('='*30)
            print(er)
            print('='*30)
        finally:
            self.mycursor.close()
            self.sql.close()

    def loginChecker(self, email, password):
        query = 'select customer_name, customer_email, customer_address, customer_contact, customer_id from customers where customer_email=%s and customer_password=md5(%s)'
        args = (email, password)
        try:
            self.mycursor.execute(query, args)
            data = self.mycursor.fetchone()
            if data:
                return data
            else:
                return False
        except Error as er:
            print('='*30)
            print(er)
            print('='*30)
        finally:
            self.mycursor.close()
            self.sql.close()


class FoodDB(Database):

    def __init__(self):
        super().__init__()
        self.mycursor.execute(
            'CREATE TABLE IF NOT EXISTS foods(food_id int AUTO_INCREMENT, food_name varchar(100) UNIQUE, food_quantity varchar(20), food_price decimal(5,2), PRIMARY KEY(food_id))')
        self.sql.commit()

    def show_all_foods(self):
        query = 'select food_id, food_name, food_quantity, food_price from foods'
        try:
            self.mycursor.execute(query)
            data = self.mycursor.fetchall()
            if data:
                return data
        except Error as er:
            print('='*30)
            print(er)
            print('='*30)
        finally:
            self.mycursor.close()
            self.sql.close()

    def order_food(self, foodId):
        query = 'select food_name, food_quantity, food_price from foods where food_id=%s'
        args = (foodId,)
        try:
            self.mycursor.execute(query, args)
            data = self.mycursor.fetchone()
            if data:
                return data
        except Error as er:
            print('='*30)
            print(er)
            print('='*30)
        finally:
            self.mycursor.close()
            self.sql.close()

    def add_food(self, foodName, quantity, price):
        query = 'insert into foods(food_name, food_quantity, food_price) values(%s,%s,%s)'
        args = (foodName, quantity, price)
        try:
            self.mycursor.execute(query, args)
            self.sql.commit()
            if self.mycursor.execute:
                return True
        except Error as er:
            print('='*30)
            print(er)
            print('='*30)
        finally:
            self.mycursor.close()
            self.sql.close()

    def update_food(self, foodName, quantity, price, foodId):
        query = 'update foods set food_name=%s, food_quantity=%s, food_price=%s where food_id=%s'
        args = (foodName, quantity, price, foodId)
        try:
            self.mycursor.execute(query, args)
            self.sql.commit()
            if self.mycursor.execute:
                return True
        except Error as er:
            print('='*30)
            print(er)
            print('='*30)
        finally:
            self.mycursor.close()
            self.sql.close()


    def delete_food(self, foodId):
        query = 'delete from foods where food_id=%s'
        args = (foodId,)
        try:
            self.mycursor.execute(query, args)
            self.sql.commit()
            if self.mycursor.execute:
                return True
        except Error as er:
            print('='*30)
            print(er)
            print('='*30)
        finally:
            self.mycursor.close()
            self.sql.close()


class OrderDB(Database):

    def __init__(self):
        super().__init__()
        self.mycursor.execute('CREATE TABLE IF NOT EXISTS orders(order_id int AUTO_INCREMENT, customer_id int, food_id int, quantity int, bill decimal(5,2), order_date datetime default now(), PRIMARY KEY(order_id), constraint custkey FOREIGN KEY (customer_id) REFERENCES customers(customer_id), constraint foodkey FOREIGN KEY (food_id) REFERENCES foods(food_id))')
        self.sql.commit()

    def show_all_orders(self):
        query = '''select c.customer_id, c.customer_name, c.customer_email, c.customer_address, c.customer_contact, 
                group_concat(f.food_name), group_concat(f.food_price), group_concat(f.food_quantity), group_concat(o.quantity), 
                group_concat(o.bill), sum(o.bill), o.order_date from customers c join orders o on 
                c.customer_id = o.customer_id join foods f on o.food_id = f.food_id group by c.customer_email, o.order_date;'''
        try:
            self.mycursor.execute(query)
            data = self.mycursor.fetchall()
            if data:
                return data
        except Error as er:
            print('='*30)
            print(er)
            print('='*30)
        finally:
            self.mycursor.close()
            self.sql.close()

    def add_order(self, customerId, foodId, quantity, bill):
        query = 'insert into orders(customer_id, food_id, quantity, bill) values(%s,%s,%s,%s)'
        args = (customerId, foodId, quantity, bill)
        try:
            self.mycursor.execute(query, args)
            self.sql.commit()
            if self.mycursor.execute:
                return True
        except Error as er:
            print('='*30)
            print(er)
            print('='*30)
        finally:
            self.mycursor.close()
            self.sql.close()

    def view_order(self, customerId):
        query = 'select order_date, group_concat(f.food_name), group_concat(f.food_quantity), group_concat(o.quantity), group_concat(bill), sum(bill) FROM foodplaza.orders as o join foods as f on f.food_id=o.food_id where o.customer_id=%s group by order_date order by order_date desc;'
        args = (customerId, )
        try:
            self.mycursor.execute(query, args)
            data = self.mycursor.fetchall()
            if data:
                return data
                # for d in data:
                #     print(d)
        except Error as er:
            print('='*30)
            print(er)
            print('='*30)
        finally:
            self.mycursor.close()
            self.sql.close()


order = OrderDB()
order.view_order(22)