# Financial Transactions Summary Tool

# Project Overview
This project processes a financial transactions dataset and produces clean summaries and visual insights. It was developed collaboratively using Agile practices, including user stories, sprint planning, and a branch-per-feature workflow.

#  Sprint Goal
Deliver a working Python tool that loads data, cleans it, generates summaries, visualizations, and passes test cases while following Agile collaboration standards.

## Project Structure
financial-transactions-summary-tool/
│
├── main.py
├── requirements.txt
├── financial_transactions.csv
│
└── src/
├── load_data.py
├── summary_functions.py
├── reports.py
│
└── tests/
└── test_transactions.py

## Features

- Reads the raw CSV file
- Removes invalid or missing records
- Standardizes column formats for consistency

- Monthly credit/debit trend line chart  
- Income vs. expense pie chart  
- Top 10 customers bar chart  
- Top 5 transactions bar chart

## User Stories (Sprint Planning)

## Tests
Run tests: pytest

### US-01 Implementation

This user story involved building the core data-loading step for the project. The team implemented the load_and_clean_data() function, which reads the raw CSV file, removes missing or invalid records, standardizes data types, and prepares a clean dataset for all other summaries and visualizations. This ensures that every feature in the tool is based on accurate and reliable data.

### US-02 - Income & Expense Summary

I implemented the calculate_income_expense() function, which computes total income from credits and total expenses from debits. This helps users understand their financial balance. I validated the results using sample transactions and ensured that the feature integrates correctly into main.py.

### US-03 - Customer Summary

In this user story, we focused on understanding how much each customer spends. We created a function that adds up all the transactions for every customer and then sorts them from the highest spender to the lowest. This helps us quickly see which customers contribute the most to the business. The results from this feature are also used later in reports and charts.

### User Story 4 – Monthly Summary:
For this user story, we created the feature that generates the monthly financial report. The function groups all transactions by month and calculates how much money came in and went out during each month. This helps users quickly understand their month-to-month financial pattern and see any changes or trends over time.

### US-05 - Visualization
This user story focused on adding visual charts to make the financial data easier to understand. We created simple graphs such as a monthly trend line chart, a pie chart for income vs expense, and bar charts for customers and high-value transactions. These visuals help users clearly see patterns instead of reading only numbers.

### Test Cases:
For this user story, we wrote a few basic test cases to make sure every part of our project works correctly. These tests help us check if the data loads properly, if the income and expense calculations are accurate, and if the customer summary, monthly report, and top transactions functions all return expected results. Running these tests gives us confidence that the tool is working as it should and helps us catch mistakes early before they cause bigger problems.

## Links 

GitHub Repository: https://github.com/barishettynaveen/Financial-transaction-summary-tool-Sec-7-Group-5

Taiga Project: https://tree.taiga.io/project/prasannapodhem-sketch-financial-transactions-summary-tool
















