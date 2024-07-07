
import re  # Import the regular expression module

# Define a class for customers
class Customer:
    # Initialize the customer with their details
    def __init__(self, first_name, last_name, residential_address, phone_number, email_address):
        self.first_name = first_name  # Set first name
        self.last_name = last_name  # Set last name
        self.residential_address = residential_address  # Set address
        self.phone_number = self.validate_phone_number(phone_number)  # Validate and set phone number
        self.email_address = self.validate_email_address(email_address)  # Validate and set email address
    
    # Function to validate phone number
    def validate_phone_number(self, phone_number):
        # Check if phone number matches the pattern
        if re.match(r'^\+?1?\d{9,15}$', phone_number):
            return phone_number  # Return valid phone number
        else:
            raise ValueError("Invalid phone number")  # Raise error for invalid phone number
    
    # Function to validate email address
    def validate_email_address(self, email_address):
        # Check if email address matches the pattern
        if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email_address):
            return email_address  # Return valid email address
        else:
            raise ValueError("Invalid email address")  # Raise error for invalid email address
    
    # Function to print customer details
    def print_details(self):
        print(f"Customer Details:\n"
              f"Name: {self.first_name} {self.last_name}\n"
              f"Residential Address: {self.residential_address}\n"
              f"Phone Number: {self.phone_number}\n"
              f"Email Address: {self.email_address}")

# Main function to create and display customer
def main():
    try:
        # Create a customer with hardcoded details
        customer = Customer(
            first_name="Shlok",
            last_name="Mathur",
            residential_address="3/31 K.C.C nagar, Ajmer road, Jaipur, Rajasthan 302026",
            phone_number="+916350207540",
            email_address="shlok@gmail.com"
        )
        customer.print_details()  # Print the details of the customer
    except ValueError as e:
        print(e)  # Print the error message if there's a ValueError

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
