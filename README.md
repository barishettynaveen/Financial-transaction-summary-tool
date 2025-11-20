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


## Links 

GitHub Repository: https://github.com/barishettynaveen/Financial-transaction-summary-tool-Sec-7-Group-5

Taiga Project: https://tree.taiga.io/project/prasannapodhem-sketch-financial-transactions-summary-tool
















