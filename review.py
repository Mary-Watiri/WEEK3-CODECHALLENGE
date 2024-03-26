# review.py

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
