# Online Retail Sales Data Pipeline

## Project Overview

This project implements a reusable ETL (Extract, Transform, Load) pipeline for processing online retail transaction data.

The pipeline extracts data from an Excel file, cleans and transforms transactions, performs feature engineering, validates the processed dataset, and exports the results in CSV and Parquet formats.

It also implements checkpointing, logging, exception handling, and DVC-based dataset version tracking.

## Objectives

- Build a reusable ETL pipeline.
- Clean and process retail transaction data.
- Handle missing values, duplicate records, cancelled invoices, and invalid prices and quantities.
- Generate transaction-level and customer-level features.
- Implement checkpointing to avoid repeating completed stages.
- Validate the processed dataset.
- Export data in CSV and Parquet formats and compare their storage efficiency.
- Track dataset versions using DVC.

## Technologies Used

- Python
- Pandas
- NumPy
- PyArrow
- Jupyter Notebook
- Git and GitHub
- DVC
- Logging and Exception Handling

## Project Structure

```text
Online_Retail_Sales_Data_Pipeline/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── checkpoints/
│
├── logs/
├── notebooks/
│   └── 01_Data_Exploration.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── validation.py
│   └── pipeline.py
│
├── .dvc/
├── .dvcignore
├── .gitignore
└── README.md
```

## ETL Workflow

1. **Extract:** Load the original Excel dataset.
2. **Clean:** Remove cancelled invoices, invalid records, and duplicate transactions; handle missing values.
3. **Transform:** Convert invoice dates and generate transaction-level and customer-level features.
4. **Checkpoint:** Save processed data for reuse.
5. **Validate:** Check data quality and feature calculations.
6. **Load:** Export the processed dataset into CSV and Parquet formats.
7. **Version Control:** Track datasets using DVC and source code using Git.

## Data Cleaning

The pipeline performs the following cleaning operations:

- Removes cancelled invoices.
- Handles invalid negative quantities and prices.
- Removes duplicate transactions.
- Fills missing product descriptions with `Unknown`.
- Retains missing CustomerID values and flags them for identification.
- Retains zero-price transactions and flags them for analysis.
- Converts invoice dates into datetime format.

Missing CustomerID records are excluded from customer-level aggregations but retained in the transaction dataset.

## Feature Engineering

The pipeline generates the following features:

| Feature | Description |
|---|---|
| TotalAmount | Quantity × UnitPrice |
| InvoiceMonth | Month of invoice |
| InvoiceYear | Year of invoice |
| InvoiceDay | Day of invoice |
| CustomerTotalOrders | Number of unique invoices per customer |
| AverageOrderValue | Average invoice value per customer |
| TotalCustomerSpending | Total spending per customer |

Customer-level features are left missing for records without a CustomerID.

## Data