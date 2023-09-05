from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from main import Customer, Restaurant, Review

# Create a database engine
engine = create_engine('sqlite:///main.db')

# Creating a database connection and session
Session = sessionmaker(bind=engine)
session = Session()

# Define a function to add data to the database
def seed_data():
    # Create a list to store instances of the model classes
    all_data = []

    # Defining the data to be added as dictionaries
    data = [
        {
            'customer': {'first_name': 'Griffin', 'last_name': 'Omondi'},
            'restaurant': {'name': 'Pizza Inn', 'price': 5},
            'review': {'star_rating': 5}
        },
        {
            'customer': {'first_name': 'John', 'last_name': 'Doe'},
            'restaurant': {'name': 'Burger King', 'price': 4},
            'review': {'star_rating': 4}
        },
        {
            'customer': {'first_name': 'Alice', 'last_name': 'Smith'},
            'restaurant': {'name': 'Sushi House', 'price': 3},
            'review': {'star_rating': 3}
        }
    ]

    # Iterating through the data to create instances
    for entry in data:
        customer = Customer(**entry["customer"])
        restaurant = Restaurant(**entry['restaurant'])
        review = Review(customer=customer, restaurant=restaurant, **entry['review'])

        all_data.extend([customer, restaurant, review])

    session.add_all(all_data)
    session.commit()

def print_deliverables():
    pass

if __name__ == "__main__":
    seed_data()
    print_deliverables()





# # creating new customer
# new_customer = Customer(first_name = "Griffin", last_name = "Omondi")
# print ("Customer's Full Name is:", new_customer.full_name())


# # # creating a new review
# restaurant_name = "Pizza Inn"
# rating = 5
# new_customer.add_review(restaurant_name,)

# #finding favorite restaurant
# favorite_restaurant = new_customer.fav_restaurant()
# if favorite_restaurant:
#     print("Favorite Restaurant:", favorite_restaurant.name)
# else:
#     print("No favorite restaurant found.")