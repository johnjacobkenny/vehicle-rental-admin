# Vehicle Rental Admin App
This project is an admin tool to manage vehicle rentals for a start-up company. The users using this system are the employees of the start-up who take requests from customers and enter it into the system. The types of vehicles available for rent include bicycle, bike, car, and boat.

## Functional requirements
Employees should be able to,
- [x] add customers
- [ ] add rental bookings (check vehicle availability, add rental booking, reduce inventory by 1)
- [x] view customer list
- [ ] view rental booking
- [x] view vehicle inventory

## Models
1. *Customer* - Name, Phone, Email
2. *Rental Booking* - Customer, Rental Date, Return Date (nullable), Vehicle Type
3. *Vehicle* - Type, Quantity

## First time setup
1. `pip install pipenv`
2. `pipenv install`

## How to run
1. `pipenv shell`
2. `python vehicle-rental-admin/main.py`

## Tasks
- [x] Setup pipenv
- [x] In the readme, give an outline about the project and requirements
- [x] Figure out project structure
- [ ] Implement the data layer
    - [x] Create db connection
    - [x] Create models
    - [ ] Implement relationships
    - [ ] Test models
- [ ] Setup initial data for the database ({‘bikes’:2, ‘cycle’:3, ’car’:1, ’boat’:2})
- [x] Implement the cli layer
- [x] Complete documentation
- [x] Push to github