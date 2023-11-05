# Jason Thomas

import csv
import sys

FILENAME = 'customers.csv'


class Customers:
    def __init__(self, customer_id, firstname, lastname, company, street, city, state, zipcode):
        self.customer_id = customer_id
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode


def read_customer_data(filename):
    customers = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            customer_id, firstname, lastname, company, street, city, state, zipcode = row
            customer = Customers(int(customer_id), firstname, lastname, company, street, city, state, zipcode)
            customers.append(customer)
    return customers


def find_customer_by_id(customers, target_id):
    for customer in customers:
        if customer.customer_id == target_id:
            return customer
    return None


def main():
    filename = 'customers.csv'
    customers = read_customer_data(filename)

    while True:
        try:
            customer_id = int(input("\nEnter customer ID to lookup or 0 to exit. \n"))
            if customer_id == 0:
                break
            customer = find_customer_by_id(customers, customer_id)
            if customer:
                print(f'{customer.firstname},{customer.lastname}')
                print(f'{customer.company}')
                print(f'{customer.street}')
                print(f'{customer.city}, {customer.state} {customer.zipcode}')
            else:
                print("Customer not found.")
        except ValueError:
            print("Please enter a valid customer ID!")


if __name__ == "__main__":
    main()
