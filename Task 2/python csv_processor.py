import csv
from datetime import datetime
import re

class Customer:
    def __init__(self, data):
        self.id = data[0]
        self.first_name = data[1]
        self.last_name = data[2]
        self.email = data[3]
        self.phone = data[4]
        self.address = data[5]
        self.city = data[6]
        self.state = data[7]
        self.zip_code = data[8]
        self.registration_date = datetime.strptime(data[9], '%Y-%m-%d')

    def __str__(self):
        return (f"Customer({self.id}, {self.first_name}, {self.last_name}, {self.email}, "
                f"{self.phone}, {self.address}, {self.city}, {self.state}, {self.zip_code}, "
                f"{self.registration_date.strftime('%Y-%m-%d')})")

    @staticmethod
    def print_customers(customers):
        for customer in customers:
            print(customer)

def read_csv(file_path):
    customers = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            customers.append(Customer(row))
    return customers

def main():
    file_path = 'customers.csv'  # Hardcoded file name
    customers = read_csv(file_path)
    Customer.print_customers(customers)

if __name__ == "__main__":
    main()
