# Create tuple with employee details
emp_details = (
    ("EmpID", input("Enter Employee ID: ")),
    ("EmpName", input("Enter Employee Name: ")),
    ("EmpAge", int(input("Enter Employee Age: "))),
    ("EmpCity", input("Enter Employee City: "))
)

# Convert tuple to dictionary
dict1 = dict(emp_details)

print("\nDictionary is:", dict1)

# Access specific values
print("\nEmployee Name is:", dict1["EmpName"])
print("Employee City is:", dict1["EmpCity"])

# Print all keys
print("\nAll Keys in Dictionary")
for x in dict1:
    print(x)

# Print all values
print("\nAll Values in Dictionary")
for x in dict1:
    print(dict1[x])

# Add new key-value pair
dict1["Phno"] = int(input("\nEnter Phone Number: "))
print("\nUpdated Dictionary is:", dict1)

# Update existing value
dict1["EmpName"] = input("\nEnter New Employee Name: ")
print("\nUpdated Dictionary is:", dict1)

# Remove a key
dict1.pop("EmpAge")
print("\nUpdated Dictionary is:", dict1)

# Length of dictionary
print("Length of Dictionary is:", len(dict1))

# Copy dictionary
dict2 = dict1.copy()
print("\nNew Dictionary is:", dict2)

# Clear dictionary
dict1.clear()
print("\nUpdated Dictionary is:", dict1)
