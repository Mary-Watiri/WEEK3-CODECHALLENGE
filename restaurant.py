# restaurant.py

from __init__ import CURSOR as cus, CONN as c

class Restaurant:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    @classmethod
    def create(cls, name, price):
        """Create a new restaurant and save it to the database."""
        try:
            restaurant = cls(None, name, price)
            restaurant.save()
            return restaurant
        except Exception as e:
            print("Error creating restaurant:", e)
            return None

        
    @classmethod
    def create_table(cls):
        """Create a new database""" 
        sql = """
            CREATE TABLE IF NOT EXISTS restaurants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price INTEGER
            )
        """
        cus.execute(sql)
        c.commit()

    def save(self):
        """Save the restaurant instance to the database."""
        sql = """
            INSERT INTO restaurants (name, price) 
            VALUES (?, ?)
        """
        cus.execute(sql, (self.name, self.price))
        c.commit()

    def reviews(self):
        # Fetch all reviews for this restaurant from the database
        sql = "SELECT * FROM reviews WHERE restaurant_id = ?"
        cus.execute(sql, (self.id,))
        reviews = cus.fetchall()
        return reviews
    
    def customers(self):
        # Fetch all customers who reviewed this restaurant from the database
        sql = """
            SELECT customers.* FROM customers 
            JOIN reviews ON customers.id = reviews.customer_id 
            WHERE reviews.restaurant_id = ?
        """
        cus.execute(sql, (self.id,))
        customers = cus.fetchall()
        return customers



# # restaurant.py

# from __init__ import CURSOR, CONN

# class Restaurant:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
        
#     @classmethod
#     def create_table(cls):
#         """Create a new database""" 
#         sql = """
#             CREATE TABLE IF NOT EXISTS restaurants (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT,
#                 price INTEGER
#             )
#         """
#         CURSOR.execute(sql)
#         CONN.commit()

#     def save(self):
#         """Save the restaurant instance to the database."""
#         sql = """
#             INSERT INTO restaurants (name, price) 
#             VALUES (?, ?)
#         """
#         CURSOR.execute(sql, (self.name, self.price))
#         CONN.commit()

#     def reviews(self):
#         # Fetch all reviews for this restaurant from the database
#         sql = "SELECT * FROM reviews WHERE restaurant_id = ?"
#         CURSOR.execute(sql, (self.id,))
#         reviews = CURSOR.fetchall()
#         return reviews
    
#     def customers(self):
#         # Fetch all customers who reviewed this restaurant from the database
#         sql = """
#             SELECT customers.* FROM customers 
#             JOIN reviews ON customers.id = reviews.customer_id 
#             WHERE reviews.restaurant_id = ?
#         """
#         CURSOR.execute(sql, (self.id,))
#         customers = CURSOR.fetchall()
#         return customers
