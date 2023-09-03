from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# defining our reviews table and specifying the content that should go in each column
class Review(Base):
    __tablename__ = 'Review'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    star_rating = Column(Integer)

# creating a full review text
def full_review(self):
    return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."