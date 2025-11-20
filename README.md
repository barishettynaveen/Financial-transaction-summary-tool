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
### US-01: Load & Clean Dataset

**As a** data analyst  
**I want to** load and clean the financial dataset  
**So that** the summaries are accurate  

**Acceptance Criteria:**
- Dataset is loaded without errors
- Missing or invalid values are handled
- Cleaned dataset is ready for further analysis

## Tests
Run tests: pytest

## Agile Collaboration

Branch-per-feature workflow

Pull requests with reviews

User story IDs used for traceability

Frequent, meaningful commits throughout the sprint

## Links 

GitHub Repository: https://github.com/barishettynaveen/Financial-transaction-summary-tool-Sec-7-Group-5

Taiga Project: https://tree.taiga.io/project/prasannapodhem-sketch-financial-transactions-summary-tool
















