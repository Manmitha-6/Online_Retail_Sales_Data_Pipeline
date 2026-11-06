# Online Retail Sales Data Pipeline

## 1. Project Overview

The **Online Retail Sales Data Pipeline** is a reusable ETL (Extract, Transform, Load) project developed to process and analyze online retail transaction data.

The pipeline extracts data from an Excel file, cleans and transforms the records, performs feature engineering, validates the processed dataset, and exports the results in CSV and Parquet formats.

The project also implements reusable Python modules, logging, exception handling, checkpointing, and DVC-based dataset version tracking.

## 2. Project Objectives

- Build a reusable ETL pipeline for retail transaction data.
- Extract data from an Excel dataset.
- Handle cancelled invoices, missing values, duplicate records, and invalid quantities and prices.
- Convert invoice dates into datetime format.
- Generate transaction-level and customer-level features.
- Implement checkpointing to reuse previously processed data.
- Include logging and exception handling.
- Validate the transformed dataset.
- Track dataset versions using DVC.
- Export processed data into CSV and Parquet formats.
- Compare the storage efficiency of both formats.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Pipeline implementation |
| Pandas | Data manipulation and processing |
| NumPy | Numerical operations |
| PyArrow | Parquet file handling |
| Jupyter Notebook | Data exploration |
| Git | Source code version control |
| GitHub | Project hosting and dataset distribution |
| DVC | Dataset version tracking |

## 4. Project Structure

```text
Online_Retail_Sales_Data_Pipeline/
|
|-- config/
|
|-- data/
|   |-- raw/
|   |-- processed/
|   |-- checkpoints/
|
|-- logs/
|
|-- notebooks/
|   |-- 01_Data_Exploration.ipynb
|
|-- reports/
|
|-- src/
|   |-- data_loader.py
|   |-- data_cleaning.py
|   |-- feature_engineering.py
|   |-- validation.py
|   |-- pipeline.py
|
|-- .dvc/
|-- .dvcignore
|-- .gitignore
|-- README.md
```

## 5. Dataset Information

The project uses the **Online Retail** transaction dataset supplied in Excel format.

- Original file: `Online Retail.xlsx`
- Original dataset dimensions: 541,909 rows and 8 columns.
- Processed dataset dimensions: 526,052 rows and 17 columns.

The dataset contains retail transaction information, including invoice numbers, product codes, descriptions, quantities, invoice dates, unit prices, customer IDs, and countries.

### Dataset Downloads

The original and processed datasets are available in the project's GitHub Release.

**Dataset Release:**

https://github.com/Manmitha-6/Online_Retail_Sales_Data_Pipeline/releases/tag/v1.0-datasets

The release contains:

- `Online Retail.xlsx` - Original dataset.
- `online_retail_features.csv` - Processed dataset in CSV format.
- `online_retail_features.parquet` - Processed dataset in Parquet format.

To reproduce the pipeline, download the original Excel file and place it inside `data/raw/` using the filename `Online Retail.xlsx`.

The processed CSV and Parquet files can be placed inside `data/processed/` when needed.

## 6. ETL Workflow

The pipeline follows these stages:

1. **Extract:** Load the original Excel dataset.
2. **Clean:** Handle cancelled invoices, invalid records, missing values, and duplicate transactions.
3. **Transform:** Convert invoice dates and generate transaction-level and customer-level features.
4. **Checkpoint:** Save intermediate processed data for reuse.
5. **Validate:** Check data quality and feature calculations.
6. **Load:** Export the final dataset into CSV and Parquet formats.
7. **Version Tracking:** Track datasets using DVC and source code using Git.

## 7. Data Cleaning

The pipeline performs the following cleaning operations:

- Removes cancelled invoices.
- Excludes records with negative quantities.
- Removes records with negative unit prices.
- Removes duplicate transactions.
- Fills missing product descriptions with `Unknown`.
- Retains records with missing CustomerID and flags them.
- Retains zero-price transactions and flags them.
- Converts InvoiceDate into datetime format.

Missing CustomerID records are retained in the transaction dataset but excluded from customer-level aggregations.

### Data Quality Summary

| Cleaning operation | Records |
|---|---:|
| Original records | 541,909 |
| Cancelled invoices removed | 9,288 |
| Negative quantity records excluded | 1,336 |
| Negative unit-price records removed | 2 |
| Duplicate records removed | 5,231 |
| Final processed records | 526,052 |

## 8. Feature Engineering

The pipeline generates the following features:

| Feature | Description |
|---|---|
| TotalAmount | Quantity multiplied by UnitPrice |
| InvoiceMonth | Month extracted from InvoiceDate |
| InvoiceYear | Year extracted from InvoiceDate |
| InvoiceDay | Day extracted from InvoiceDate |
| CustomerTotalOrders | Number of unique invoices per customer |
| AverageOrderValue | Average invoice value per customer |
| TotalCustomerSpending | Total spending per customer |

Customer-level features are left missing for records without a CustomerID.

## 9. Data Validation

The processed dataset is checked for data quality and consistency.

The final validation results are:

| Validation check | Result |
|---|---:|
| Dataset shape | 526,052 x 17 |
| Missing required columns | 0 |
| Duplicate rows | 0 |
| Negative quantities | 0 |
| Negative prices | 0 |
| Cancelled invoices | 0 |
| Invalid invoice date type | False |
| TotalAmount calculation errors | 0 |

All the listed validation checks passed successfully.

## 10. Checkpointing and Logging

### Checkpointing

The pipeline saves intermediate processing results so that completed stages can be reused instead of repeating the entire process unnecessarily.

### Logging

Logging is implemented to record pipeline execution information and help identify processing issues.

### Exception Handling

Exception handling is included to manage errors during data processing and pipeline execution.

## 11. DVC and Git Version Tracking

The project uses:

- **Git and GitHub:** To track source code and project files.
- **DVC:** To track dataset versions using DVC metadata and `.dvc` files.

The dataset files are also distributed through the GitHub Release.

**Note:** A DVC remote has not been configured. Therefore, downloading the datasets from the GitHub Release is the current dataset retrieval method. `dvc pull` is not configured for this project.

## 12. CSV and Parquet Comparison

The final processed dataset is exported in both CSV and Parquet formats.

| Format | File size |
|---|---:|
| CSV | 69.00 MB |
| Parquet | 4.25 MB |

Parquet provides a smaller storage size for this dataset.

**Storage reduction: 93.84%**

This comparison demonstrates the storage efficiency of Parquet for the processed retail dataset.

## 13. How to Run the Project

### Prerequisites

- Python
- Anaconda
- Required Python libraries
- Git and DVC

### Step 1: Clone the Repository

```bash
git clone https://github.com/Manmitha-6/Online_Retail_Sales_Data_Pipeline.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Online_Retail_Sales_Data_Pipeline
```

### Step 3: Prepare the Dataset

Download `Online Retail.xlsx` from the GitHub Release and place it inside:

```text
data/raw/
```

### Step 4: Run the Pipeline

From the project root, execute:

```bash
cd notebooks
python -c "import sys; sys.path.insert(0, '../src'); from pipeline import run_pipeline; df = run_pipeline(); print(df.shape)"
```

The pipeline processes the dataset, performs validation, and exports the final CSV and Parquet files.

## 14. Expected Output

The completed pipeline produces:

- Cleaned retail transaction data.
- Transaction-level and customer-level features.
- Validated processed dataset.
- CSV export.
- Parquet export.
- Processing checkpoints.
- Execution logs.

Final processed dataset dimensions:

```text
(526052, 17)
```

## 15. Conclusion

The Online Retail Sales Data Pipeline demonstrates how a reusable ETL workflow can be developed to process real-world retail transaction data.

It combines data extraction, cleaning, transformation, feature engineering, validation, checkpointing, logging, and dataset version tracking.

The project also demonstrates the storage efficiency of Parquet compared with CSV, providing a structured and reusable approach to retail data processing.