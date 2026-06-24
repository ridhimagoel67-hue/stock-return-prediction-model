# Stock Return Prediction Using Financial Statement Analytics

## Overview

This project predicts future stock returns using company fundamentals, valuation metrics, ownership patterns, and financial statement data. The objective is to identify financial indicators associated with stock performance and build machine learning models capable of estimating future returns.

The project follows an end-to-end machine learning workflow covering data preparation, feature engineering, model development, evaluation, and deployment through an interactive Streamlit application.

---

## Problem Statement

Traditional stock analysis requires evaluating a large number of financial indicators across thousands of companies. This project aims to automate that process by leveraging machine learning techniques to estimate future stock returns from historical financial and market data.

### Target Variable

```python
future_return = (future_price - current_price) / current_price
```

---

## Dataset

The dataset was constructed by combining multiple financial datasets, including:

- Balance Sheet Data
- Profit & Loss Statements
- Cash Flow Statements
- Financial Ratios
- Ownership Metrics
- Historical Market Prices

### Final Dataset

- 90+ financial features
- Financial, valuation, profitability, liquidity, and ownership indicators

---

## Project Workflow

```text
Raw Financial Data
        ↓
Data Cleaning
        ↓
Missing Value Treatment
        ↓
Feature Engineering
        ↓
Feature Selection
        ↓
Model Training
        ↓
Hyperparameter Tuning
        ↓
Model Evaluation
        ↓
Streamlit Deployment
```

---

## Exploratory Data Analysis

Performed extensive EDA to understand:

- Missing value patterns
- Feature distributions
- Outliers
- Correlation structure
- Relationships between company fundamentals and future returns

---

## Feature Engineering

Created a feature-rich dataset using company fundamentals, valuation metrics, ownership patterns, and financial ratios.

### Top Features

- Debt to Equity Ratio
- Price to Earnings Ratio (P/E)
- Return on Assets (ROA)
- Return on Equity (ROE)
- Dividend Yield
- Change in FII Holding
- G Factor
- Number of Shareholders
- Current Price
- Debtor Days
- Graham Number
- Price to Book Value
- Working Capital (5 Years Back)
- Quick Ratio
- Return on Capital Employed (ROCE)

---

## Models Evaluated

The following regression models were trained and compared:

- Linear Regression
- K-Nearest Neighbors Regressor
- Random Forest Regressor
- Extra Trees Regressor
- XGBoost Regressor
- CatBoost Regressor

Hyperparameter tuning was performed to improve model performance and generalization.

---

## Results

### Best Model: CatBoost Regressor

| Metric | Score |
|----------|----------|
| R² Score | 0.3815 |
| MAE | 0.0446 |
| RMSE | 0.0566 |

### Key Findings

- Ensemble-based models significantly outperformed baseline regression approaches.
- Profitability metrics such as ROE and ROA showed strong predictive power.
- Valuation indicators including P/E and P/B ratios contributed substantially to model performance.
- Ownership-related metrics such as FII holding changes provided additional predictive signal.
- Feature selection improved interpretability while reducing noise from less informative variables.

---

## Deployment

The final model was deployed as an interactive Streamlit application that allows users to input company financial metrics and obtain predicted future stock returns.

### Application Features

- Real-time prediction generation
- Financial metric input interface
- Interactive prediction dashboard
- Model-driven return estimation

### Live Demo

https://stock-return-prediction-model.streamlit.app/

---

## Technology Stack

### Programming

- Python

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-Learn
- XGBoost
- CatBoost

### Deployment

- Streamlit

### Version Control

- Git
- GitHub

---

## Repository Structure

```text
├── app/
├── data/
├── models/
├── notebooks/
├── images/
├── requirements.txt
└── README.md
```
---