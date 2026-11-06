\# Data Quality Report

\## Online Retail Sales Data Pipeline



\### 1. Report Overview



This report documents the data cleaning and validation performed on the Online Retail transaction dataset as part of the Online Retail Sales Data Pipeline project.



The objective is to ensure that the processed dataset is consistent, accurate, and suitable for retail sales and customer analysis.



\### 2. Dataset Information



| Description | Details |

|---|---|

| Dataset | Online Retail |

| Original file | Online Retail.xlsx |

| Original records | 541,909 |

| Original columns | 8 |

| Final processed records | 526,052 |

| Final processed columns | 17 |

| Output formats | CSV and Parquet |



\### 3. Data Cleaning Operations



The following cleaning operations were performed:



1\. Removed cancelled invoices.

2\. Excluded transactions with negative quantities.

3\. Removed records with negative unit prices.

4\. Removed duplicate transactions.

5\. Replaced missing product descriptions with `Unknown`.

6\. Retained missing CustomerID records and added a missing-value indicator.

7\. Retained zero-price transactions and added a zero-price indicator.

8\. Converted InvoiceDate into datetime format.



\### 4. Data Cleaning Summary



| Cleaning operation | Records |

|---|---:|

| Original records | 541,909 |

| Cancelled invoices removed | 9,288 |

| Negative quantity records excluded | 1,336 |

| Negative unit-price records removed | 2 |

| Duplicate records removed | 5,231 |

| Final processed records | 526,052 |



\### 5. Missing Value Handling



\- Missing product descriptions were replaced with `Unknown`.

\- Records with missing CustomerID were retained.

\- `IsCustomerIDMissing` was added to identify missing customer IDs.

\- Customer-level aggregate features were not calculated for records without a CustomerID.



\### 6. Data Validation Results



The final processed dataset was checked using custom validation rules.



| Validation check | Result |

|---|---:|

| Dataset shape | 526,052 × 17 |

| Missing required columns | 0 |

| Duplicate rows | 0 |

| Negative quantities | 0 |

| Negative unit prices | 0 |

| Cancelled invoices | 0 |

| Invalid invoice date type | False |

| TotalAmount calculation errors | 0 |



\### 7. Feature Validation



The following engineered features were included:



\- TotalAmount

\- InvoiceMonth

\- InvoiceYear

\- InvoiceDay

\- CustomerTotalOrders

\- AverageOrderValue

\- TotalCustomerSpending



The TotalAmount feature was checked against the calculation:



`TotalAmount = Quantity × UnitPrice`



No calculation errors were found.



\### 8. Final Data Quality Summary



The final dataset contains 526,052 records and 17 columns.



All listed validation checks passed successfully:



\- No duplicate rows remain.

\- No negative quantities remain.

\- No negative unit prices remain.

\- No cancelled invoices remain.

\- InvoiceDate has the correct datetime type.

\- TotalAmount calculations are valid.



\### 9. Conclusion



The Online Retail dataset was successfully cleaned, transformed, and validated through the reusable ETL pipeline.



The resulting dataset is suitable for retail transaction analysis, customer-level analysis, and further data processing.

