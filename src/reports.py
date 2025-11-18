def monthly_report(df):
    df['month'] = df['date'].dt.to_period('M').astype(str)
    return df.groupby(['month', 'type'])['amount'].sum().unstack(fill_value=0)

def top_transactions(df, n=5):
    return df.sort_values(by='amount', ascending=False).head(n)

