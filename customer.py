from __init__ import CURSOR as cus, CONN as c

class Customer:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        
    @classmethod
    def create_table(cls):
        """Create the customers table."""
        try:
            sql = """
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT,
                    last_name TEXT
                )
            """
            cus.execute(sql)
            c.commit()
            print("Customers table created successfully.")
        except Exception as e:
            print("Error creating customers table:", e)

    def save(self):
        """Save the customer instance to the database."""
        try:
            sql = """
                INSERT INTO customers (first_name, last_name) 
                VALUES (?, ?)
            """
            cus.execute(sql, (self.first_name, self.last_name))
            c.commit()
            print("Customer saved successfully.")
        except Exception as e:
            print("Error saving customer:", e)

    @classmethod
    def create(cls, first_name, last_name):
        """Create a new customer and save it to the database."""
        try:
            customer = cls(None, first_name, last_name)  
            customer.save()
            return customer
        except Exception as e:
            print("Error creating customer:", e)
            return None

    def reviews(self):
        """Return a collection of all the reviews that the customer has left."""
        try:
            # Importing Review here to avoid circular dependency
            from review import Review
            
            sql = "SELECT * FROM reviews WHERE customer_id = ?"
            cus.execute(sql, (self.id,))
            reviews_data = cus.fetchall()
            return [Review(*row) for row in reviews_data]
        except Exception as e:
            print("Error fetching reviews for customer:", e)
            return []
    @classmethod
    def get_by_id(cls, customer_id):
        """Retrieve a customer by their ID."""
        try:
            sql = "SELECT * FROM customers WHERE id = ?"
            cus.execute(sql, (customer_id,))
            customer_data = cus.fetchone()
            if customer_data:
                return cls(*customer_data)
            else:
                return None
        except Exception as e:
            print("Error fetching customer by ID:", e)
            return None
    def favorite_restaurant(self):
        """Return the restaurant instance that has the highest star rating from this customer."""
        try:
            # Retrieve all reviews made by this customer
            customer_reviews = self.reviews()

            if customer_reviews:
                # Find the review with the highest star rating
                highest_rating_review = max(customer_reviews, key=lambda review: review.star_rating)
                # Get the restaurant ID from the highest rated review
                restaurant_id = highest_rating_review.restaurant_id
                # Retrieve the restaurant instance with the highest rated review
                favorite_restaurant = Restaurant.get_by_id(restaurant_id)
                return favorite_restaurant
            else:
                print("No reviews found for this customer.")
                return None
        except Exception as e:
            print("Error fetching favorite restaurant for customer:", e)
            return None  
    
    def full_name(self):
        """Return the full name of the customer."""
        return f"{self.first_name} {self.last_name}"
    
    @classmethod
    def find_by_id(cls, customer_id):
        """Retrieve a customer by their ID."""
        try:
            sql = "SELECT * FROM customers WHERE id = ?"
            cus.execute(sql, (customer_id,))
            customer_data = cus.fetchone()
            if customer_data:
                return cls(*customer_data)
            else:
                return None
        except Exception as e:
            print("Error fetching customer by ID:", e)
            return None
        
    def delete(self):
        """Delete the customer from the database."""
        try:
            sql = "DELETE FROM customers WHERE id = ?"
            cus.execute(sql, (self.id,))
            c.commit()
            print("Customer deleted successfully.")
        except Exception as e:
            print("Error deleting customer:", e)
            
    @classmethod
    def customer_full_name(cls, id):
        """Retrieve and print the full name of a customer by their ID."""
        try:
            customer = cls.get_by_id(id)
            if customer:
                print(customer.full_name())
            else:
                print("Customer not found")
        except Exception as e:
            print("Error fetching customer full name:", e)