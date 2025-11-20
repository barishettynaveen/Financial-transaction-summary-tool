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

### Load & Clean Dataset
- Reads the raw CSV file
- Removes invalid or missing records
- Standardizes column formats for consistency

### Income & Expense Summary
- Calculates total income (credits)
- Calculates total expenses (debits)

### Monthly Report
- Groups all transactions by month
- Computes monthly totals for credits and debits

### Customer-Level Summary
- Ranks customers by total spending
- Generates a top 10 customer spending report

### Top Transactions
- Identifies the highest-value financial transactions

### Visual Charts
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
---

### **US-02: Calculate Income & Expense**
**As a** financial analyst  
**I want to** compute total income and expenses  
**So that** I can understand overall financial balance  
**Acceptance Criteria:**  
- Function returns total income  
- Function returns total expenses  
- Values match dataset calculations  

---

### **US-03: Monthly Summary**
**As a** user  
**I want to** see monthly debit and credit totals  
**So that** I can track trends over time  
**Acceptance Criteria:**  
- Monthly totals are grouped correctly  
- Debit and credit columns calculated per month  
- Returns a clean summary DataFrame  

---

### **US-04: Customer Summary**
**As a** business owner  
**I want to** see the top spending customers  
**So that** I understand customer value and behavior  
**Acceptance Criteria:**  
- Customers ranked by total spending  
- Top 10 list generated successfully  
- Output sorted in descending order  

---

### **US-05: Visualizations**
**As a** viewer  
**I want to** see graphical charts of financial activity  
**So that** insights are easy to understand  
**Acceptance Criteria:**  
- Line chart for credit/debit trend  
- Pie chart for income vs expense  
- Bar chart for top 10 customers  
- Bar chart for top 5 transactions  
- All charts render without errors  

---

## User Story Assignments

| User Story | Description | Assigned Member |
|-----------|-------------|-----------------|
| **US-01 – Data Cleaning** | Load and clean the financial dataset | **Ravindra** |
| **US-02 – Income & Expense Summary** | Compute total income and total expenses | **Prasanna Podhem** |
| **US-03 – Customer Summary** | Generate spending summary and top customers | **Naveen** |
| **US-04 – Monthly Report** | Produce monthly credit/debit summary | **Deep** |
| **US-05 – Visualizations** | Create charts for trends and insights | **Naveen** |
| **Test Cases** | Implement pytest test cases | **Ravindra** |
| **Main Script Integration** | Connect all functions inside `main.py` | **Prasanna** |
| **Documentation** | README, structure, and explanations | **Deep Patel** |

----

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
















