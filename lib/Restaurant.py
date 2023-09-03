from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# creating the restaurant model defining the restaurants columns and their contents
class Restaurant(Base):
    __table__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

# setting up relationships
# reviews to restaurants many to one relationship
# customer to restaurants many to many relationship
    reviews = relationship('Review', back_populates='restaurant')
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants')

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

# creating a database connection and session
engine = create_engine('sqlite:///restaurant_reviews.db')
Session = sessionmaker(bind=engine)
session = Session()