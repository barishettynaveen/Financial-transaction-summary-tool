import pandas as pd

# Load dataset
df = pd.read_csv("financial_transactions.csv")

# Display basic info
print("📊 Dataset Summary:")
print(df.info())
print("\nFirst 5 Rows:")
print(df.head())

# Handle missing values
df = df.fillna(0)

# Calculate totals
total_income = df[df["Type"].str.lower() == "income"]["Amount"].sum()
total_expense = df[df["Type"].str.lower() == "expense"]["Amount"].sum()
net_balance = total_income - total_expense

# Display results
print("\n💰 Financial Summary:")
print(f"Total Income: ${total_income:,.2f}")
print(f"Total Expenses: ${total_expense:,.2f}")
print(f"Net Balance: ${net_balance:,.2f}")

# Export cleaned data if needed
df.to_csv("cleaned_financial_transactions.csv", index=False)
