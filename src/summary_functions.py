
def calculate_income_expense(df):
    """
    Calculates total income (credit) and total expenses (debit).
    """

    income = df[df["type"] == "credit"]["amount"].sum()
    expense = df[df["type"] == "debit"]["amount"].sum()

    return {
        "total_income": income,
        "total_expense": expense
    }
