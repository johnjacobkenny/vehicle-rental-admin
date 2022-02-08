from .db import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"{self.name}, {self.phone}, {self.email}"


class Booking(Base):
    __tablename__ = "booking"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"), nullable=False)
    rental_date = Column(DateTime, nullable=False)
    return_date = Column(DateTime)
    vehicle_type_id = Column(Integer, ForeignKey("vehicle.id"), nullable=False)


class Vehicle(Base):
    __tablename__ = "vehicle"

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"{self.type}, {self.quantity}"
