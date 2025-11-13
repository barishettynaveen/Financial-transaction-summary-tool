
import pandas as pd
import matplotlib.pyplot as plt


# 1. Load the dataset

df = pd.read_csv("Downloads/financial_transactions.csv")


# 2. Basic info

print("Dataset Summary:")
print(df.info())
print("\nFirst 5 Rows:")
print(df.head())


# 3. Cleaning / preprocessing


# Clean text in 'type' column (e.g., ' Credit ' -> 'credit')
df["type"] = df["type"].astype(str).str.lower().str.strip()

# Ensure 'amount' is numeric
df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0)


# 4. Core financial summaries

total_income = df[df["type"] == "credit"]["amount"].sum()
total_expense = df[df["type"] == "debit"]["amount"].sum()
net_balance = total_income - total_expense

print("\n Financial Summary:")
print(f"Total Income:  ${total_income:,.2f}")
print(f"Total Expense: ${total_expense:,.2f}")
print(f"Net Balance:   ${net_balance:,.2f}")


# 5. Optional: summary by type

type_summary = df.groupby("type")["amount"].sum().reset_index()
print("\n Amount by Transaction Type:")
print(type_summary)


# 6. Optional: Visualization

labels = ["Total Credit (Income)", "Total Debit (Expense)"]
values = [total_income, total_expense]

plt.figure(figsize=(6, 4))
plt.bar(labels, values)
plt.title("Income vs Expense Summary")
plt.ylabel("Amount")
plt.tight_layout()
plt.show()


