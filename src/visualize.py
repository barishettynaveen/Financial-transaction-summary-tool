# 3. Visualizations
import matplotlib.pyplot as plt

# Visualization: Monthly Trend

# Visualization: Line Chart

monthly = monthly_report(df)

plt.figure(figsize=(10, 5))

plt.plot(monthly.index, monthly["credit"], marker="o", label="Credit (Income)")
plt.plot(monthly.index, monthly["debit"], marker="o", label="Debit (Expense)")

plt.title("Monthly Credit and Debit Trend")
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()



# Visualization: Income vs Expense (Pie)

income_expense = calculate_income_expense(df)

labels = ["Total Income", "Total Expense"]
sizes = [
    income_expense["total_income"],
    income_expense["total_expense"],
]

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Income vs Expense Distribution")
plt.show()


# Visualization: Top 10 Customers


top_customers = customer_summary(df).head(10)

top_customers.plot(
    kind="bar",
    figsize=(10, 5),
    color="skyblue"
)
plt.title("Top 10 Customers by Total Spending")
plt.xlabel("Customer ID")
plt.ylabel("Total Amount ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualization: Top 5 Highest Transactions


top5 = top_transactions(df)

plt.figure(figsize=(8, 5))
plt.bar(top5["transaction_id"].astype(str), top5["amount"])
plt.title("Top 5 Transactions by Amount")
plt.xlabel("Transaction ID")
plt.ylabel("Amount ($)")
plt.tight_layout()
plt.show()


