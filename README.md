# Alpha Insurance Analysis

## Overview
This project focuses on analyzing insurance claims data to identify risk patterns, detect anomalies, and build predictive models. The analysis includes statistical testing, feature engineering, and machine learning models to improve risk assessment and fraud detection.

## Table of Contents
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Installation](#installation)
- [Data Preprocessing](#data-preprocessing)
- [Statistical Analysis](#statistical-analysis)
- [Machine Learning Models](#machine-learning-models)
- [Results](#results)
- [Interpreability](#Interpreability)


## Dataset
The dataset consists of insurance claims data with attributes such as:
- `CustomerID` - Unique identifier for each customer
- `Province` - Region of the customer
- `PostalCode` - Postal code of the customer
- `Gender` - Gender of the customer
- `TotalClaims` - Total number of claims filed
- `ClaimAmount` - Amount claimed
- `Date` - Date of the claim

## Installation
To set up the project environment, run:
```bash
# Clone the repository
git clone https://github.com/yitayalk/alpha-insurance-analysis.git
cd alpha-insurance-analysis

# Create a virtual environment
python -m venv alivenv
source alivenv/bin/activate  # On Windows use `alivenv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Data Preprocessing
- Handle missing values and outliers
- Convert date columns to numerical features
- Encode categorical variables using one-hot encoding
- Normalize numerical features

## Statistical Analysis
- **T-Test**: Used to compare `TotalClaims` across different provinces
- **Z-Test**: Applied for large sample hypothesis testing
- **Chi-Square Test**: Analyzed categorical relationships between `Gender` and `ClaimAmount`

## Machine Learning Models
- **Linear Regression**: Predicts `ClaimAmount`
- **Random Forest**: Improves prediction accuracy and feature importance analysis

## Results
- **Statistical testing** found no significant differences in claim patterns based on `Province`, `PostalCode`, and `Gender`.
- **Machine Learning Models** improved claim prediction, with Random Forest performing better than Linear Regression.
- **Time-Series Models** provided insights into claim seasonality and volatility.
