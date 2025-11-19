def monthly_report(df):
    """
    Generates a monthly summary of credit and debit totals.
    """

    df["month"] = df["date"].dt.to_period("M").astype(str)

    report = (
        df.groupby(["month", "type"])["amount"]
        .sum()
        .unstack(fill_value=0)
    )

    return report


def top_transactions(df, n=5):
    """
    Returns the top n highest transactions.
    """

    return df.sort_values(by="amount", ascending=False).head(n)
