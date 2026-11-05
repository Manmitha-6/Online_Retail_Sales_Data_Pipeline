
import logging

logger = logging.getLogger(__name__)


def validate_retail_data(df):
    """
    Validate the cleaned and feature-engineered retail dataset.
    """

    try:
        logger.info("Starting dataset validation.")

        required_columns = [
            "InvoiceNo",
            "StockCode",
            "Description",
            "Quantity",
            "InvoiceDate",
            "UnitPrice",
            "CustomerID",
            "Country",
            "IsZeroPrice",
            "IsCustomerIDMissing",
            "TotalAmount",
            "InvoiceMonth",
            "InvoiceYear",
            "InvoiceDay",
            "CustomerTotalOrders",
            "AverageOrderValue",
            "TotalCustomerSpending"
        ]

        # 1. Check required columns
        missing_columns = [
            col for col in required_columns
            if col not in df.columns
        ]

        if missing_columns:
            raise ValueError(
                f"Missing required columns: {missing_columns}"
            )

        # 2. Check duplicate records
        duplicates = df.duplicated().sum()

        # 3. Check invalid quantities and prices
        negative_quantities = (df["Quantity"] < 0).sum()
        negative_prices = (df["UnitPrice"] < 0).sum()

        # 4. Check cancelled invoices
        cancelled_invoices = (
            df["InvoiceNo"].astype(str).str.startswith("C").sum()
        )

        # 5. Check invoice date format
        invalid_dates = (
            not df["InvoiceDate"].dtype.kind == "M"
        )

        # 6. Check TotalAmount calculation
        expected_amount = (
            df["Quantity"] * df["UnitPrice"]
        )

        amount_errors = (
            (df["TotalAmount"] - expected_amount).abs() > 0.000001
        ).sum()

        # 7. Prepare validation report
        report = {
            "Dataset Shape": df.shape,
            "Missing Required Columns": missing_columns,
            "Duplicate Rows": int(duplicates),
            "Negative Quantities": int(negative_quantities),
            "Negative Prices": int(negative_prices),
            "Cancelled Invoices": int(cancelled_invoices),
            "Invalid Date Type": invalid_dates,
            "TotalAmount Errors": int(amount_errors)
        }

        logger.info("Dataset validation completed.")

        return report

    except Exception:
        logger.exception("Dataset validation failed.")
        raise
