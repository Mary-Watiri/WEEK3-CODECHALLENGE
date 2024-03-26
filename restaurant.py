from __init__ import CURSOR as cus, CONN as c
from review import Review

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
        # Importing Customer here to avoid circular dependency
        from customer import Customer
        
        # Fetch all reviews for this restaurant from the database
        sql = "SELECT * FROM reviews WHERE restaurant_id = ?"
        cus.execute(sql, (self.id,))
        reviews = cus.fetchall()
        return reviews
    
    def customers(self):
        # Importing Customer here to avoid circular dependency
        from customer import Customer
        
        # Fetch all customers who reviewed this restaurant from the database
        sql = """
            SELECT customers.* FROM customers 
            JOIN reviews ON customers.id = reviews.customer_id 
            WHERE reviews.restaurant_id = ?
        """
        cus.execute(sql, (self.id,))
        customers = cus.fetchall()
        return customers
    
    @classmethod
    def fanciest(cls):
        """Return the fanciest restaurant (restaurant with the highest price)."""
        try:
            sql = """
                SELECT * FROM restaurants
                ORDER BY price DESC
                LIMIT 1
            """
            cus.execute(sql)
            result = cus.fetchone()
            if result:
                return cls(*result)
            else:
                return None
        except Exception as e:
            print("Error fetching the fanciest restaurant:", e)
            return None

    def all_reviews(self):
        """Return a list of strings with all the reviews for this restaurant."""
        try:
            # Importing Customer here to avoid circular dependency
            from customer import Customer
            
            sql = "SELECT * FROM reviews WHERE restaurant_id = ?"
            cus.execute(sql, (self.id,))
            reviews_data = cus.fetchall()
            formatted_reviews = []
            for row in reviews_data:
                customer = Customer.get_by_id(row[2])
                customer_name = customer.full_name() if customer else "Unknown Customer"
                formatted_review = f"Review for {self.name} by {customer_name}: {row[4]} stars."
                formatted_reviews.append(formatted_review)
            return formatted_reviews
        except Exception as e:
            print("Error fetching reviews for restaurant:", e)
            return []

    def delete(self):
        # Delete restaurant from the database
        sql = """DELETE FROM restaurants WHERE id = ?"""
        cus.execute(sql, (self.id,))
        c.commit()
        
    @classmethod
    def find_by_id(cls, id):
        """Retrieve a restaurant by its ID."""
        try:
            sql = "SELECT * FROM restaurants WHERE id = ?"
            cus.execute(sql, (id,))
            restaurant_data = cus.fetchone()
            if restaurant_data:
                return cls(*restaurant_data)
            else:
                return None
        except Exception as e:
            print("Error fetching restaurant by ID:", e)
            return None
        
    @classmethod
    def restaurant_fanciest(cls):
        """Return the fanciest restaurant (restaurant with the highest price)."""
        try:
            sql = """
                SELECT * FROM restaurants
                ORDER BY price DESC
                LIMIT 1
            """
            cus.execute(sql)
            result = cus.fetchone()
            if result:
                return cls(*result)
            else:
                return None
        except Exception as e:
            print("Error fetching the fanciest restaurant:", e)
            return None
