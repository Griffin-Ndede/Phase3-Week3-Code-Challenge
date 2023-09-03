from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    # defining the table and setting the columns and contents
    __tablename__ = 'customers'

    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)

    # # customers are related to restaurants since they write reviews for restaurants
    # reviews = relationship('Review', back_populates= 'customer')
    # # keeping track of which restaurant a customer likes
    # restaurants = relationship('Restaurant', secondary = 'reviews', back_populates = 'customers')

    # concatenate first and last name and returns the value
    def full_name(self):
        return f"{self.first_name}, {self.last_name}"
    
    # finding the restaurant a customer likes the most
    def fav_restaurant(self):
        favorite = max(self.reviews, key = lambda review: review.star_rating, default=None)
        if favorite:
            return favorite.restaurant
        return None
    
    # creating a review for the restaurant
    def add_review(self, restaurant, rating):
        new_review = Review(customer = self, restaurant = restaurant, star_rating = rating)
        session.add(new_review)
        session.commit()

    def delete_review(self, restaurant):
        reviews_to_delete = [review for review in self.reviews if review.restautant == restaurant]
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()

# creating a database connection and session
engine = create_engine('sqlite:///restaurant_reviews.db')
Session = sessionmaker(bind=engine)
session = Session()

 # creating new customer
new_customer = Customer(first_name = "Griffin", last_name = "Omondi")
print ("Customer's Full Name is:", new_customer.full_name())


# # creating a new review
# restaurant_name = "Pizza Inn"
# rating = 5
# new_customer.add_review(restaurant_name,)

#finding favorite restaurant
favorite_restaurant = new_customer.fav_restaurant()
if favorite_restaurant:
    print("Favorite Restaurant:", favorite_restaurant.name)
else:
    print("No favorite restaurant found.")