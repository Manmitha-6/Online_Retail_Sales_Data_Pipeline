
import pandas as pd
import logging

logger = logging.getLogger(__name__)


def create_transaction_features(df):
    """
    Create transaction-level features.
    """

    try:
        logger.info("Creating transaction features.")

        df = df.copy()

        # Calculate total transaction amount
        df["TotalAmount"] = (
            df["Quantity"] * df["UnitPrice"]
        )

        # Extract date features
        df["InvoiceDate"] = pd.to_datetime(
            df["InvoiceDate"]
        )

        df["InvoiceMonth"] = df["InvoiceDate"].dt.month
        df["InvoiceYear"] = df["InvoiceDate"].dt.year
        df["InvoiceDay"] = df["InvoiceDate"].dt.day

        logger.info("Transaction features created successfully.")

        return df

    except Exception:
        logger.exception("Error creating transaction features.")
        raise


def create_customer_features(df):
    """
    Create customer-level features.
    """

    try:
        logger.info("Creating customer features.")

        df = df.copy()

        # Use only records with a known CustomerID
        customer_data = df.dropna(
            subset=["CustomerID"]
        )

        # Count unique invoices for each customer
        customer_order_counts = (
            customer_data.groupby("CustomerID")["InvoiceNo"]
            .nunique()
        )

        df["CustomerTotalOrders"] = df["CustomerID"].map(
            customer_order_counts
        )

        # Calculate total amount for each customer invoice
        customer_invoice_totals = (
            customer_data.groupby(
                ["CustomerID", "InvoiceNo"]
            )["TotalAmount"]
            .sum()
        )

        # Calculate average order value per customer
        customer_avg_order_value = (
            customer_invoice_totals.groupby("CustomerID")
            .mean()
        )

        df["AverageOrderValue"] = df["CustomerID"].map(
            customer_avg_order_value
        )

        # Calculate total spending per customer
        customer_spending = (
            customer_data.groupby("CustomerID")["TotalAmount"]
            .sum()
        )

        df["TotalCustomerSpending"] = df["CustomerID"].map(
            customer_spending
        )

        logger.info("Customer features created successfully.")

        return df

    except Exception:
        logger.exception("Error creating customer features.")
        raise
