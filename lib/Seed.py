from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from main import Customer, Restaurant, Review

# Create a database engine
engine = create_engine('sqlite:///main.db')

# Creating a database connection and session
Session = sessionmaker(bind=engine)
session = Session()

# Define a function to add data to the database
# Define a function to add data to the database
def seed_data():
    # Create a list to store instances of the model classes
    all_data = []

    # Define a lists to store instances of the models
    customer_instances = []
    restaurant_instances = []
    review_instances = []

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

        # Append instances to the lists
        customer_instances.append(customer)
        restaurant_instances.append(restaurant)
        review_instances.append(review)

    session.add_all(all_data)
    session.commit()

    # Print customer names
    for customer_instance in customer_instances:
        print(customer_instance.full_name())
    
    # print restaurant names
    for restaurant_instances in restaurant_instances:
        print(restaurant_instances.name, restaurant_instances.reviews)

    # printint reviews
    for review_instances in review_instances:
        print(review_instances.full_review)

    # creating a new customer
if __name__ == "__main__":
    seed_data()