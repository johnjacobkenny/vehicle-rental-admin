from re import T
from xmlrpc.client import TRANSPORT_ERROR
from .db import Base
from sqlalchemy import Column, Integer, String, DateTime

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)

class Booking(Base):
    __tablename__ = "booking"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, nullable=False)
    rental_date = Column(DateTime, nullable=False)
    return_date = Column(DateTime)
    vehicle_type = Column(Integer, nullable=False)

class Vehicle(Base):
    __tablename__ = "vehicle"

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)