import re

# Phone number validation
phone = input("Enter your phone number (format XXX-XXX-XXXX): ")
phone_pattern = r"^\d{3}-\d{3}-\d{4}$"

if re.match(phone_pattern, phone):
    print("Phone number is valid!")
else:
    print("Invalid phone number format!")

# Password validation
password = input("Enter your password: ")
password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"

if re.match(password_pattern, password):
    print("Strong password!")
else:
    print("Weak password! Make sure it has at least 8 characters, including:")
    print(" - 1 uppercase letter")
    print(" - 1 lowercase letter")
    print(" - 1 digit")
