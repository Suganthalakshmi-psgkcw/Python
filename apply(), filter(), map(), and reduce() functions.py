import pandas as pd
from functools import reduce

# Create data
data = {
    "Name": ["Ravi", "Anu", "Kiran", "Meena"],
    "Age": [30, 22, 45, 19],
    "Income": [40000, 28000, 50000, 30000],
    "CreditScore": [720, 680, 750, 600],
    "LoanAmount": [300000, 200000, 400000, 150000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Filter eligible customers
eligible = df[
    (df["Age"] >= 21) &
    (df["Income"] >= 25000) &
    (df["CreditScore"] >= 650) &
    (df["LoanAmount"] <= df["Income"] * 10)
].copy()   # important to avoid warning

# Calculate Processing Fee (2%)
eligible["ProcessingFee"] = eligible["LoanAmount"].map(lambda x: x * 0.02)

# Add Loan Status
eligible["LoanStatus"] = eligible.apply(
    lambda row: "Approved", axis=1
)

# Calculate total approved loan
total_loan = reduce(
    lambda x, y: x + y,
    eligible["LoanAmount"]
)

# Output
print("Eligible Customers:\n")
print(eligible)

print("\nTotal Approved Loan Amount:", total_loan)
