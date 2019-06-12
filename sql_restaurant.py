#beginning configuration file
import sys
from sqlalchemy import Column, ForeignKey, Integer, String 
from sqlalchemy.ext.declarative import declarative_base #for config and class code
from sqlalchemy.orm import relationship # for foreign key reationships
from sqlalchemy import create_engine

Base = declarative_base() # to let sqlalchemy know that our classes are special sqlalchemy classes coresponding to tables in our db

## Classes 
class Restaurant(Base):
    ### table information
    __tablename__ = 'restaurant'
    ## mapper
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)

class MenuItem(Base):
    ## Table information
    __tablename__ = 'menu_item'
    ## mapper
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)  
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)# relationship to the class Retaurant 

## ending configuartion code
engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.create_all(engine)# adds classes we shall be using in the db as new tables
