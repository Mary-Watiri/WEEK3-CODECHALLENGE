from __init__ import CURSOR as cus, CONN as c

class Review:
    @classmethod
    def create_table(cls):
        """Create the reviews table."""
        try:
            sql = """
                CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    review TEXT,
                    customer_id INTEGER,
                    restaurant_id INTEGER,
                    star_rating INTEGER,
                    FOREIGN KEY (customer_id) REFERENCES customers(id),
                    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
                )
            """
            cus.execute(sql)
            c.commit()
            print("Reviews table created successfully.")
        except Exception as e:
            print("Error creating reviews table:", e)
            
    def __init__(self, id, review_text, customer_id, restaurant_id, star_rating):
        self.id = id
        self.review_text = review_text
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        self.star_rating = star_rating

    def full_review(self, customer_name, restaurant_name):
        """Return a formatted string representing the full review."""
        return f"Review for {restaurant_name} by {customer_name}: {self.star_rating} stars."

    @classmethod
    def create(cls, review, customer_id, restaurant_id, star_rating):
        """Create a new review instance and save it to the database."""
        try:
            review_instance = cls(None, review, customer_id, restaurant_id, star_rating)
            review_instance.save()
            return review_instance
        except Exception as e:
            print("Error creating review:", e)
            return None
            
    def save(self):
        """Save the review instance to the database."""
        try:
            sql = """
                INSERT INTO reviews (review, customer_id, restaurant_id, star_rating) 
                VALUES (?, ?, ?, ?)
            """
            cus.execute(sql, (self.review_text, self.customer_id, self.restaurant_id, self.star_rating))
            c.commit()
            print("Review saved successfully.")
        except Exception as e:
            print("Error saving review:", e)
        
    @classmethod
    def instance_from_db(cls, row):
        """Create a review instance from the database row."""
        try:
            review = cls(row[0], row[1], row[2], row[3], row[4])
            return review
        except Exception as e:
            print("Error creating review instance from DB row:", e)
            return None
    
    @classmethod
    def find_by_id(cls, id):
        """Retrieve a review by its ID."""
        try:
            sql = "SELECT * FROM reviews WHERE id = ?"
            row = cus.execute(sql, (id,)).fetchone()
            return cls.instance_from_db(row) if row else None
        except Exception as e:
            print("Error fetching review by ID:", e)
            return None

    def delete(self):
        """Delete the review from the database."""
        try:
            sql = "DELETE FROM reviews WHERE id = ?"
            cus.execute(sql, (self.id,))
            c.commit() 
            print("Review deleted successfully")
        except Exception as e:
            print("Error deleting review:", e)

    def reviews(self):
        """Retrieve all reviews left by the customer."""
        try:
            sql = "SELECT * FROM reviews WHERE customer_id = ?"
            cus.execute(sql, (self.customer_id,))
            rows = cus.fetchall()
            reviews = [Review.instance_from_db(row) for row in rows]
            return reviews
        except Exception as e:
            print("Error fetching reviews:", e)
            return []

