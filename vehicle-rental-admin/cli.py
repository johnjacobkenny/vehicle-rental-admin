def menu_main():
    print()
    print("Rental Admin App")
    print("--------------------")
    print("1. Add customer")
    print("2. Add rental booking")
    print("3. See customer list")
    print("4. See rental booking list")
    print("5. See vehicle inventory list")
    print("6. Quit")
    return int(input("Choose an option: "))


def menu_add_rental():
    pass


def get_customer_details():
    print()
    name = input("Enter customer name: ")
    phone = input("Enter customer phone: ")
    email = input("Enter customer email: ")

    return (name, phone, email)


def print_customer_details(customers):
    print()
    print("CUSTOMERS")
    print("Name, Phone, Email")
    print("--------------")
    for customer in customers:
        print(customer)
    print()


def get_vehicle_details():
    print()
    vehicle_type = input("Enter vehicle type: ")
    quantity = input("Enter quantity: ")

    return (vehicle_type, quantity)


def print_vehicle_details(vehicles):
    print()
    print("VEHICLE INVENTORY")
    print("Type, Quantity")
    print("--------------")
    for vehicle in vehicles:
        print(vehicle)
    print()


def print_rental_details(rentals):
    print()
    print("Rental bookings")
    print("--------------")
    for rental in rentals:
        print(rental)
    print()
