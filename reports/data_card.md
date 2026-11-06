\# Data Card

\## Online Retail Sales Data Pipeline



\### 1. Dataset Overview



| Field | Description |

|---|---|

| Dataset Name | Online Retail |

| Source | UCI Machine Learning Repository |

| File Format | Excel (.xlsx) |

| Original File | Online Retail.xlsx |

| Original Records | 541,909 |

| Original Columns | 8 |

| Final Processed Records | 526,052 |

| Final Processed Columns | 17 |

| Output Formats | CSV and Parquet |



\### 2. Dataset Purpose



The dataset contains online retail transactions. It is used in this project to build an automated ETL pipeline for cleaning transaction records, generating business features, and preparing data for customer and sales analysis.



\### 3. Data Description



The original dataset contains the following fields:



| Column | Description |

|---|---|

| InvoiceNo | Invoice number identifying a transaction |

| StockCode | Product code |

| Description | Product description |

| Quantity | Number of units purchased |

| InvoiceDate | Date and time of the transaction |

| UnitPrice | Price per unit |

| CustomerID | Customer identifier |

| Country | Customer's country |



\### 4. Data Processing



The dataset was processed using Python and Pandas.



The following operations were performed:



\- Removed cancelled invoices.

\- Excluded transactions with negative quantities.

\- Removed records with negative unit prices.

\- Removed duplicate transactions.

\- Handled missing product descriptions.

\- Retained missing CustomerID records with an indicator column.

\- Retained zero-price transactions with an indicator column.

\- Converted InvoiceDate into datetime format.



\### 5. Engineered Features



The processed dataset includes these additional features:



\- TotalAmount

\- InvoiceMonth

\- InvoiceYear

\- InvoiceDay

\- CustomerTotalOrders

\- AverageOrderValue

\- TotalCustomerSpending



\### 6. Data Quality



The final dataset was validated to ensure:



\- No duplicate rows.

\- No negative quantities.

\- No negative unit prices.

\- No cancelled invoices.

\- Correct InvoiceDate data type.

\- Correct TotalAmount calculations.



\### 7. Known Limitations



\- Some transactions do not contain CustomerID.

\- Customer-level aggregate features are unavailable for records with missing CustomerID.

\- Zero-price transactions are retained and identified using a separate indicator.

\- The dataset represents historical transactions and may not reflect current retail activity.



\### 8. Intended Uses



The processed dataset can be used for:



\- Retail sales analysis.

\- Customer purchasing behavior analysis.

\- Order value analysis.

\- Customer spending analysis.

\- Further data analytics and machine learning projects.



\### 9. Ethical Considerations



The dataset contains transaction information. Customer identifiers should be handled responsibly, and the data should not be used to identify or contact individual customers.



\### 10. Conclusion



The Online Retail dataset was cleaned, transformed, and validated through a reusable ETL pipeline. The processed data is available in CSV and Parquet formats for further analysis.

