from db import session
from db.models import Customer, Vehicle, Booking
from cli import get_customer_details, get_vehicle_details, print_vehicle_details, print_customer_details, menu_main, print_rental_details


def handle_main_menu():
    response = 0
    while(response != 6):
        response = menu_main()
        if response == 1:
            add_customer()
        elif response == 2:
            # in progress
            pass
        elif response == 3:
            get_customers()
        elif response == 4:
            # in progress
            pass
        elif response == 5:
            get_vehicles()


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

    # booking = Booking(customer_id=1, rental_date=datetime.datetime.now(), return_date=None, vehicle_type_id=1)

    # session.add(booking)
    # session.commit()


def get_rental_bookings():
    print_rental_details(session.query(Booking).all())
