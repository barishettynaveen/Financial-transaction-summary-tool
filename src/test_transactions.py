from src.load_data import load_and_clean_data
from src.summary_functions import calculate_income_expense

def test_load_data():
    df = load_and_clean_data("financial_transactions.csv")
    assert 'date' in df.columns
    assert df['date'].dtype.name in ['datetime64[ns]', 'datetime64[ns, UTC]']

def test_income_expense():
    df = load_and_clean_data("financial_transactions.csv")
    result = calculate_income_expense(df)
    assert "total_income" in result
    assert "total_expense" in result


