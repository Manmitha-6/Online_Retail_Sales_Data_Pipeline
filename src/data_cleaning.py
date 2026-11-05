
import pandas as pd
import logging

logger = logging.getLogger(__name__)


def clean_retail_data(df):
    """
    Clean the Online Retail dataset.
    """

    try:
        logger.info("Starting data cleaning.")

        df_clean = df.copy()

        initial_rows = len(df_clean)

        # 1. Remove cancelled invoices
        df_clean = df_clean[
            ~df_clean["InvoiceNo"].astype(str).str.startswith("C")
        ].copy()

        # 2. Remove negative quantity adjustment records
        adjustment_mask = (
            (df_clean["Quantity"] < 0) &
            (df_clean["UnitPrice"] == 0) &
            (df_clean["CustomerID"].isna())
        )

        df_clean = df_clean[~adjustment_mask].copy()

        # 3. Remove negative prices
        df_clean = df_clean[df_clean["UnitPrice"] >= 0].copy()

        # 4. Remove duplicate rows
        df_clean = df_clean.drop_duplicates().copy()

        # 5. Handle missing descriptions
        df_clean["Description"] = (
            df_clean["Description"].fillna("Unknown")
        )

        # 6. Flag zero-price transactions
        df_clean["IsZeroPrice"] = (
            df_clean["UnitPrice"] == 0
        )

        # 7. Flag missing customer IDs
        df_clean["IsCustomerIDMissing"] = (
            df_clean["CustomerID"].isna()
        )

        logger.info(
            "Cleaning completed. Initial rows: %s, Final rows: %s",
            initial_rows,
            len(df_clean)
        )

        return df_clean

    except Exception:
        logger.exception("Error during data cleaning.")
        raise
