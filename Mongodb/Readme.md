Run the Script:

sh
Copy code
python csv_processor.py
Expected Output:
The script will perform the following operations:

Read the customers.csv file and create Customer objects.
Insert the customers into the MongoDB database.
Fetch and print all customers from the database.
Update the last name of the customer with ID 1 and print the updated customer.
Delete the customer with ID 1 and print the remaining customers.
The output will display the customer details at each step, demonstrating the CRUD operations.

Code Explanation
Customer Class
Attributes:

id: Customer ID.
first_name: First name of the customer.
last_name: Last name of the customer.
email: Email address of the customer.
phone: Phone number of the customer.
address: Residential address of the customer.
city: City of residence.
state: State of residence.
zip_code: ZIP code of residence.
registration_date: Registration date of the customer.
Methods:

__init__(self, data): Initializes a new customer instance from a list of data.
to_dict(self): Converts the customer object to a dictionary for MongoDB insertion.
__str__(self): Returns a string representation of the customer.
print_customers(customers): Prints a list of customer instances.
Database Functions
read_csv(file_path): Reads a CSV file and returns a list of Customer instances.
insert_customers_to_db(customers): Inserts multiple customer objects into the MongoDB collection.
fetch_all_customers(): Fetches all customers from the MongoDB collection and returns them as a list of Customer objects.
update_customer(customer_id, update_fields): Updates a customer's details in MongoDB.
delete_customer(customer_id): Deletes a customer from MongoDB by their ID.
Main Function
The main function demonstrates the usage of the Customer class and database functions. It performs the following steps:

Reads the CSV file and creates Customer objects.
Inserts the customers into the MongoDB database.
Fetches and prints all customers from the database.
Updates the last name of the customer with ID 1 and prints the updated customer.
Deletes the customer with ID 1 and prints the remaining customers.
Full Code
python
Copy code
import csv
from datetime import datetime
import re
from pymongo import MongoClient

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

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "registration_date": self.registration_date
        }

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

def insert_customers_to_db(customers):
    client = MongoClient('localhost', 27017)
    db = client['customer_db']
    collection = db['customers']
    collection.insert_many([customer.to_dict() for customer in customers])

def fetch_all_customers():
    client = MongoClient('localhost', 27017)
    db = client['customer_db']
    collection = db['customers']
    customers = collection.find()
    return [Customer([cust['id'], cust['first_name'], cust['last_name'], cust['email'], cust['phone'], cust['address'], cust['city'], cust['state'], cust['zip_code'], cust['registration_date'].strftime('%Y-%m-%d')]) for cust in customers]

def update_customer(customer_id, update_fields):
    client = MongoClient('localhost', 27017)
    db = client['customer_db']
    collection = db['customers']
    collection.update_one({"id": customer_id}, {"$set": update_fields})

def delete_customer(customer_id):
    client = MongoClient('localhost', 27017)
    db = client['customer_db']
    collection = db['customers']
    collection.delete_one({"id": customer_id})

def main():
    file_path = 'customers.csv'  # Hardcoded file name
    customers = read_csv(file_path)
    insert_customers_to_db(customers)
    print("Customers inserted to MongoDB.")

    # Fetch and print all customers
    all_customers = fetch_all_customers()
    Customer.print_customers(all_customers)

    # Update a customer
    update_customer("1", {"last_name": "UpdatedDoe"})
    print("\nCustomer with ID 1 after update:")
    updated_customer = fetch_all_customers()
    Customer.print_customers(updated_customer)

    # Delete a customer
    delete_customer("1")
    print("\nAll customers after deleting customer with ID 1:")
    remaining_customers = fetch_all_customers()
    Customer.print_customers(remaining_customers)

if __name__ == "__main__":
    main()
Running the Program
Ensure MongoDB is running on your local machine.
Save the script as csv_processor.py.
Save the CSV data as customers.csv in the same directory.
Run the script by executing the following command in your terminal: