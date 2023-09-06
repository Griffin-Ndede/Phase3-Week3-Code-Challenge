
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# creating a session and engine 
engine = create_engine('sqlite:///main.db')
session = sessionmaker(bind=engine)
session = session()

# creating a base class for declarative base
Base = declarative_base()

# defining the table and setting the columns and contents
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)

    # customers are related to restaurants since they write reviews for restaurants
    reviews = relationship('Review', back_populates= 'customer')


    # concatenate first and last name and returns the value
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
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
    
    # deleting a restaurant
    def delete_review(self, restaurant):
        reviews_to_delete = [review for review in self.reviews if review.restautant == restaurant]
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()


        # creating the restaurant model defining the restaurants columns and their contents
class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

# setting up relationships
# reviews to restaurants many to one relationship
# customer to restaurants many to many relationship
    reviews = relationship('Review', back_populates='restaurant')

# finding the fanciest restaurant by querying for highest priced restaurant
@classmethod
def fancy(cls):
    return session.query(cls).order_by(cls.price.desc()).first()    

# getting all the reviews from a restaurant and formatting them
def all_reviews(self):
    formatted_reviews =[]
    for review in self.reviews:
        formatted_review = f"Review for {self.name} by {review.customer.full_name()}: {review.star_rating} stars."
        formatted_reviews.append(formatted_review)
    return formatted_review

# defining our reviews table and specifying the content that should go in each column
class Review(Base):
    __tablename__ = 'Review'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    star_rating = Column(Integer)

    # defining the relationship between the review module and the other modules
    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='reviews')

# creating a full review text
def full_review(self):
    return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."


# creating a database connection and session
Base.metadata.create_all(engine)