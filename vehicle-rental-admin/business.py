from db import session
from db.models import Customer, Vehicle
from cli import get_customer_details, get_vehicle_details, print_vehicle_details, print_customer_details, menu_main

def handle_main_menu():
    response = 0
    while(response != 6):
        response = menu_main()


def add_customer():
    (name, phone, email) = get_customer_details()

    customer = Customer(name=name, phone=phone, email=email)
    session.add(customer)
    session.commit()


def get_customers():
    print_customer_details(session.query(Customer).all())


def add_vehicle():
    (vehicle_type, quantity) = get_vehicle_details()
    vehicle = Vehicle(type=vehicle_type, quantity=quantity)
    session.add(vehicle)
    session.commit()


def get_vehicles():
    print_vehicle_details(session.query(Vehicle).all())


def add_booking():
    pass
    # ask for customer name
    # if customer doesn't exist, then ask again

    # ask for vehicle type
    # if selected vehicle type quantity is 0, then mention that vehicle is not available, do they want to try with another vehicle, or just cancel booking
