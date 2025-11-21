import pandas as pd
from src.load_data import load_and_clean_data
from src.summary_functions import calculate_income_expense, customer_summary
from src.reports import monthly_report, top_transactions

def test_load_data():
    df = load_and_clean_data("financial_transactions.csv")
    assert pd.api.types.is_datetime64_any_dtype(df["date"])
    assert set(df["type"].unique()).issubset({"credit", "debit"})

def test_income_expense():
    df = load_and_clean_data("financial_transactions.csv")
    result = calculate_income_expense(df)
    assert "total_income" in result
    assert "total_expense" in result

def test_customer_summary():
    df = load_and_clean_data("financial_transactions.csv")
    summary = customer_summary(df)
    assert len(summary) > 0

def test_monthly_report():
    df = load_and_clean_data("financial_transactions.csv")
    report = monthly_report(df)
    assert len(report) > 0

def test_top_transactions():
    df = load_and_clean_data("financial_transactions.csv")
    top5 = top_transactions(df)
    assert len(top5) == 5
