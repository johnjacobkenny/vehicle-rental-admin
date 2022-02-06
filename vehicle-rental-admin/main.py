from db import session
from db.models import Customer
from cli.customer import get_customer_details


def add_customer():
    (name, phone, email) = get_customer_details()

    customer = Customer(name=name, phone=phone, email=email)
    session.add(customer)
    session.commit()

# message = models.Messages(message="Hello world")

# session.add(message)
# session.commit()

# query = session.query(Messages)

# instance = query.first()
# print(instance.message)


add_customer()
