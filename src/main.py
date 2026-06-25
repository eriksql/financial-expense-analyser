import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("../data/expenses.csv")

print("FINANCIAL EXPENSE ANALYZER\n")

# Total expenses
total_expenses = df["amount"].sum()
print(f"Total Expenses: ${total_expenses:.2f}")

# Average expense
average_expense = df["amount"].mean()
print(f"Average Expense: ${average_expense:.2f}")

# Expenses by category
category_totals = df.groupby("category")["amount"].sum()

print("\nExpenses by Category:")
print(category_totals)

# Highest category
highest_category = category_totals.idxmax()

print(f"\nHighest Category: {highest_category}")

# Create chart
category_totals.plot(kind="bar")

plt.title("Expenses by Category")
plt.ylabel("Amount ($)")
plt.tight_layout()

plt.savefig("../output/expenses_chart.png")

plt.show()