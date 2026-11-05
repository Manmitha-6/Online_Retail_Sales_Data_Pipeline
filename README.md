# Online Retail Sales Data Pipeline

## Project Overview

This project implements a reusable ETL (Extract, Transform, Load) pipeline for processing online retail transaction data.

The pipeline extracts data from an Excel file, cleans and transforms the transactions, performs feature engineering, validates the processed dataset, and exports the results in CSV and Parquet formats.

It also implements checkpointing, logging, exception handling, and DVC-based dataset version tracking.

## Objectives

- Build a reusable ETL pipeline.
- Clean and process retail transaction data.
- Handle missing values, duplicate records, cancelled invoices, and invalid prices and quantities.
- Generate transaction-level and customer-level features.
- Implement checkpointing to avoid repeating completed stages.
- Validate the processed dataset.
- Export data in CSV and Parquet formats.
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
3. **Transform:** Convert invoice dates and generate transaction and customer features.
4. **Checkpoint:** Save processed data for reuse.
5. **Validate:** Check data quality and feature calculations.
6. **Load:** Export the processed dataset into CSV and Parquet formats.
7. **Version Control:** Track datasets using DVC and source code using Git.

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

## Data Validation Results

Final processed dataset:

- Rows: 526,052
- Columns: 17
- Duplicate rows: 0
- Negative quantities: 0
- Negative prices: 0
- Cancelled invoices: 0
- TotalAmount calculation errors: 0

## Output Formats

The pipeline exports:

- `online_retail_features.csv`
- `online_retail_features.parquet`

Both formats contain the same processed dataset. Parquet provides a more storage-efficient columnar format.

## How to Run the Project

### 1. Install dependencies

```bash
pip install pandas numpy pyarrow python-calamine jupyterlab dvc
```

### 2. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 3. Prepare the dataset

Place the original `Online Retail.xlsx` file inside:

```text
data/raw/
```

If the dataset is already available in your local DVC cache, restore it using DVC.

### 4. Run the pipeline

Open Anaconda Prompt in the project directory and run:

```bash
cd notebooks
```

Then execute:

```bash
python -c "import sys; sys.path.insert(0, '../src'); from pipeline import run_pipeline; df = run_pipeline(); print(df.shape)"
```

### 5. Check the output

The processed CSV and Parquet files will be saved in:

```text
data/processed/
```

## Dataset Versioning

DVC is used to track the original Excel dataset and the processed CSV and Parquet datasets.

Git tracks the source code, notebooks, configuration, and DVC tracking files.

## Conclusion

This project demonstrates an end-to-end retail data processing workflow using Python, Pandas, reusable modules, data validation, checkpointing, and dataset version control.
