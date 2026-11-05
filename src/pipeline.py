
import os
import logging
import pandas as pd

from data_loader import load_excel
from data_cleaning import clean_retail_data
from feature_engineering import (
    create_transaction_features,
    create_customer_features
)
from validation import validate_retail_data


# --------------------------------------------------
# 1. Configure logging
# --------------------------------------------------

LOG_FOLDER = "../logs"
os.makedirs(LOG_FOLDER, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_FOLDER, "pipeline.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

logger = logging.getLogger(__name__)


# --------------------------------------------------
# 2. Main ETL Pipeline
# --------------------------------------------------

def run_pipeline(
    raw_path="../data/raw/Online Retail.xlsx",
    checkpoint_path="../data/checkpoints/retail_features_checkpoint.csv",
    processed_folder="../data/processed"
):

    """
    Complete Online Retail ETL Pipeline.

    1. Extract data from Excel.
    2. Clean transaction data.
    3. Generate transaction features.
    4. Generate customer features.
    5. Save and reuse checkpoints.
    6. Validate the dataset.
    7. Export CSV and Parquet files.
    """

    try:

        logger.info("Retail data pipeline started.")

        # Create required folders
        checkpoint_dir = os.path.dirname(checkpoint_path)

        if checkpoint_dir:
            os.makedirs(checkpoint_dir, exist_ok=True)

        os.makedirs(processed_folder, exist_ok=True)

        # --------------------------------------------------
        # Step 1: Checkpoint loading or complete ETL
        # --------------------------------------------------

        if os.path.exists(checkpoint_path):

            logger.info("Existing checkpoint found.")

            df_clean = pd.read_csv(
                checkpoint_path,
                dtype={
                    "InvoiceNo": "string",
                    "StockCode": "string"
                },
                parse_dates=["InvoiceDate"]
            )

            logger.info("Checkpoint loaded successfully.")

        else:

            # Step 2: Extract
            logger.info("Extracting original Excel dataset.")

            df = load_excel(raw_path)

            # Step 3: Clean
            logger.info("Cleaning transaction data.")

            df_clean = clean_retail_data(df)

            # Step 4: Transaction feature engineering
            logger.info("Generating transaction features.")

            df_clean = create_transaction_features(df_clean)

            # Step 5: Customer feature engineering
            logger.info("Generating customer features.")

            df_clean = create_customer_features(df_clean)

            # Step 6: Convert mixed identifiers to strings
            df_clean["InvoiceNo"] = df_clean["InvoiceNo"].astype("string")
            df_clean["StockCode"] = df_clean["StockCode"].astype("string")

            # Step 7: Save checkpoint
            df_clean.to_csv(
                checkpoint_path,
                index=False
            )

            logger.info("Checkpoint saved successfully.")

        # Ensure consistent identifier types after checkpoint loading too
        df_clean["InvoiceNo"] = df_clean["InvoiceNo"].astype("string")
        df_clean["StockCode"] = df_clean["StockCode"].astype("string")

        # --------------------------------------------------
        # Step 8: Validate
        # --------------------------------------------------

        logger.info("Validating processed dataset.")

        validation_report = validate_retail_data(df_clean)

        print("\nFINAL VALIDATION REPORT")

        for check, result in validation_report.items():
            print(f"{check}: {result}")

        # --------------------------------------------------
        # Step 9: Export CSV and Parquet
        # --------------------------------------------------

        csv_path = os.path.join(
            processed_folder,
            "online_retail_features.csv"
        )

        parquet_path = os.path.join(
            processed_folder,
            "online_retail_features.parquet"
        )

        logger.info("Exporting processed dataset to CSV.")

        df_clean.to_csv(
            csv_path,
            index=False
        )

        logger.info("Exporting processed dataset to Parquet.")

        df_clean.to_parquet(
            parquet_path,
            engine="pyarrow",
            index=False
        )

        # --------------------------------------------------
        # Step 10: Pipeline completion
        # --------------------------------------------------

        logger.info("CSV and Parquet exports completed.")
        logger.info("Retail data pipeline completed successfully.")

        print("\nPIPELINE COMPLETED SUCCESSFULLY!")
        print("Final dataset shape:", df_clean.shape)
        print("CSV saved at:", csv_path)
        print("Parquet saved at:", parquet_path)

        return df_clean

    except Exception:

        logger.exception("Retail data pipeline failed.")

        raise
