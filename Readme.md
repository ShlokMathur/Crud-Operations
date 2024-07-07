# Customer Class

## Overview
This program models a `Customer` class with basic customer information and validation features for phone number and email address.

## Customer Class

### Attributes
- `first_name`: First name of the customer.
- `last_name`: Last name of the customer.
- `address`: Residential address of the customer.
- `phone`: Phone number of the customer (validated).
- `email`: Email address of the customer (validated).

### Methods
- `__init__(self, first_name, last_name, address, phone, email)`: Initializes a new customer instance and validates the phone number and email address.
- `validate_phone(self, phone)`: Validates the phone number.
- `validate_email(self, email)`: Validates the email address.
- `print_details(self)`: Prints the customer details.

### Validation
- **Phone Number**: Must match the regex pattern `^\+?1?\d{9,15}$`.
- **Email Address**: Must match the regex pattern `^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$`.

## Usage

### Main Function
The main function demonstrates the usage of the `Customer` class by creating an instance with hardcoded details and printing the customer details.

```python
def main():
    try:
        # Create a Customer instance with hardcoded details
        customer = Customer(
            first_name="John",
            last_name="Doe",
            address="1234 Elm Street, Springfield, IL",
            phone="+11234567890",
            email="john.doe@example.com"
        )
        # Print customer details
        customer.print_details()
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
