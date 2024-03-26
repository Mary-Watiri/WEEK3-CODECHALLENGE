from customer import Customer
from restaurant import Restaurant
from review import Review

if __name__ == "__main__":
    # Create tables if they don't exist
    Review.create_table()
    Customer.create_table()
    Restaurant.create_table()

    # Create sample customers
    customer1 = Customer.create("John", "Kamau")
    customer2 = Customer.create("Jane", "Muthoni")

    # Create sample restaurants
    restaurant1 = Restaurant.create("Carnivore", 100)
    restaurant2 = Restaurant.create("Java House", 200)

    # Create sample reviews
    review1 = Review.create("Amazing nyama choma!", customer1.id, restaurant1.id, 5)
    review2 = Review.create("Great coffee and ambiance.", customer2.id, restaurant2.id, 4)

    # Retrieve and display information
    # Assuming you have the customer_id stored in the review object
    review3 = Review.create("Excellent service!", customer1.id, restaurant2.id, 5)

    # Access the customer object associated with the review
    customer = Customer.get_by_id(review1.customer_id)

    # Check if the customer object exists
    if customer:
        print("Review 1 Customer Full Name:", customer.full_name())
    else:
        print("Customer not found for review.")
        
    # Retrieve the favorite restaurant for customer1
    favorite_restaurant = customer1.favorite_restaurant()
    if favorite_restaurant:
        print(f"{customer1.full_name()}'s favorite restaurant is:", favorite_restaurant.name)
    else:
        print("No favorite restaurant found for", customer1.full_name())
    
    def full_review(self):
        """Return a formatted string representing the full review."""
        try:
            # Retrieve the restaurant name associated with the review
            restaurant = Restaurant.get_by_id(self.restaurant_id)
            restaurant_name = restaurant.name if restaurant else "Unknown Restaurant"

            # Retrieve the customer's full name associated with the review
            customer = Customer.get_by_id(self.customer_id)
            customer_full_name = customer.full_name() if customer else "Unknown Customer"

            # Retrieve the star rating of the review
            star_rating = self.star_rating

            # Format the string
            return f"Review for {restaurant_name} by {customer_full_name}: {star_rating} stars."
        except Exception as e:
            print("Error fetching review details:", e)
            return "Error retrieving review details"
        
review = Review.find_by_id(1)

review = Review.find_by_id(23)
if review:
    review.delete()
    print("Review deleted successfully")
else:

    print("Review not found")

customer = Customer.find_by_id(1)
if customer:
    customer.delete()
    print("Customer deleted successfully")
else:

    print("Customer not found")
restaurant = Restaurant.find_by_id(1)
if restaurant:
    restaurant.delete()
    print("Restaurant deleted successfully")
else:

    print("Restaurant not found")
Restaurant.restaurant_fanciest()
Customer.customer_full_name(2)