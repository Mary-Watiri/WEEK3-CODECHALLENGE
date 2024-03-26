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
