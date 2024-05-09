# # Abdijalilov Suxrob
# ID19732
# N42 guruh


# # =========> 1-savol
# import psycopg2
#
# db_connection_info = {
#     "host": "localhost",
#     "database": "n42",
#     "user": "postgres",
#     "password": "1234",
#     "port": "5432"
# }
#
# create_table_query = """
# CREATE TABLE Product (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100) NOT NULL UNIQUE,
#     price NUMERIC(10, 2),
#     color VARCHAR(50) NOT NULL ,
#     image VARCHAR(255) NOT NULL
# );
# """
#
# try:
#
#     connection = psycopg2.connect(**db_connection_info)
#
#     cursor = connection.cursor()
#
#     cursor.execute(create_table_query)
#
#     connection.commit()
#
#     print("Product jadvali muvaffaqiyatli yaratildi!")
#
# except (Exception, psycopg2.DatabaseError) as error:
#     print("Xatolik yuz berdi:", error)
#
# finally:
#     if connection:
#         cursor.close()
#         connection.close()
# # =========> 2-savol
# import psycopg2
#
# db_connection_info = {
#     "host": "localhost",
#     "database": "n42",
#     "user": "postgres",
#     "password": "1234",
# "port": "5432"
#
#
#
# def insert_product(name, price, color, image):
#     try:
#         connection = psycopg2.connect(**db_connection_info)
#         cursor = connection.cursor()
#         insert_query = "INSERT INTO Product (name, price, color, image) VALUES (%s, %s, %s, %s)"
#         cursor.execute(insert_query, (name, price, color, image))
#         connection.commit()
#         print("Mahsulot muvaffaqiyatli qo'shildi!")
#     except (Exception, psycopg2.DatabaseError) as error:
#         print("Xatolik yuz berdi:", error)
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()
#
#
# def select_all_products():
#     try:
#         connection = psycopg2.connect(**db_connection_info)
#         cursor = connection.cursor()
#         select_query = "SELECT * FROM Product"
#         cursor.execute(select_query)
#         products = cursor.fetchall()
#         for product in products:
#             print(product)
#     except (Exception, psycopg2.DatabaseError) as error:
#         print("Xatolik yuz berdi:", error)
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()
#
#
# def update_product(product_id, name, price, color, image):
#     try:
#         connection = psycopg2.connect(**db_connection_info)
#         cursor = connection.cursor()
#         update_query = "UPDATE Product SET name=%s, price=%s, color=%s, image=%s WHERE id=%s"
#         cursor.execute(update_query, (name, price, color, image, product_id))
#         connection.commit()
#         print("Mahsulot ma'lumotlari muvaffaqiyatli yangilandi!")
#     except (Exception, psycopg2.DatabaseError) as error:
#         print("Xatolik yuz berdi:", error)
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()
#
#
# def delete_product(product_id):
#     try:
#         connection = psycopg2.connect(**db_connection_info)
#         cursor = connection.cursor()
#         delete_query = "DELETE FROM Product WHERE id=%s"
#         cursor.execute(delete_query, (product_id,))
#         connection.commit()
#         print("Mahsulot muvaffaqiyatli o'chirildi!")
#     except (Exception, psycopg2.DatabaseError) as error:
#         print("Xatolik yuz berdi:", error)
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()

# =========> 3-savol
# class Alphabet:
#     def __init__(self):
#         self.letters = "abcdefghijklmnopqrstuvwxyz"
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.letters):
#             current_letter = self.letters[self.index]
#             self.index += 1
#             return current_letter
#         else:
#             raise StopIteration
#
#
# alpha = Alphabet()
#
#
# for letter in alpha:
#     print(letter)
# ========>4-savol
# import threading
# import time
#
#
# def print_numbers():
#     for num in range(1, 6):
#         print(num)
#         time.sleep(1)
#
#
# def print_letters():
#     for letter in "ABCDE":
#         print(letter)
#         time.sleep(1)
#
#
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print("Barcha threadinglar tugadi.")
# ======> 5-savol
# import psycopg2
#
# db_connection_info = {
#     "host": "localhost",
#     "database": "n42",
#     "user": "postgres",
#     "password": "1234",
#     "port": "5432"
# }
#
#
# class Product:
#     def __init__(self, name, price, color, image):
#         self.name = name
#         self.price = price
#         self.color = color
#         self.image = image
#
#     def save(self):
#         try:
#             connection = psycopg2.connect(**db_connection_info)
#             cursor = connection.cursor()
#             insert_query = "INSERT INTO Product (name, price, color, image) VALUES (%s, %s, %s, %s)"
#             cursor.execute(insert_query, (self.name, self.price, self.color, self.image))
#             connection.commit()
#             print("Mahsulot muvaffaqiyatli saqlandi!")
#         except (Exception, psycopg2.DatabaseError) as error:
#             print("Xatolik yuz berdi:", error)
#         finally:
#             if connection:
#                 cursor.close()
#                 connection.close()
#
#
# product1 = Product("Telefon", 1000, "Qora", "telefon_image.jpg")
# product1.save()
#
# product2 = Product("Kompyuter", 1500, "Oq", "kompyuter_image.jpg")
# product2.save()
# ========> 6-savol
import psycopg2

class DbConnect:
    def __init__(self, connection_info):
        self.connection_info = connection_info

    def __enter__(self):
        self.conn = psycopg2.connect(**self.connection_info)
        self.cur = self.conn.cursor()
        return self.conn, self.cur

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.commit()
            self.conn.close()


db_connection_info = {
    "host": "localhost",
    "database": "n42",
    "user": "postgres",
    "password": "1234",
    "port": "5432"
}

with DbConnect(db_connection_info) as (conn, cur):
    cur.execute("SELECT * FROM Product")
    rows = cur.fetchall()
    for row in rows:
        print(row)
