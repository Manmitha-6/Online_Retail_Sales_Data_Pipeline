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

## 6. ET