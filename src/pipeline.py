
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


# Configure logging
logging.basicConfig(
    filename="../logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def run_pipeline(
    raw_path="../data/raw/Online Retail.xlsx",
    checkpoint_path="../data/checkpoints/retail_features_checkpoint.csv",
    processed_folder="../data/processed"
):
    """
    Run the complete retail data processing pipeline.
    Uses an existing checkpoint when available.
    """

    try:
        logger.info("Retail data pipeline started.")

        os.makedirs(os.path.dirname(checkpoint_path), exist_ok=True)
        os.makedirs(processed_folder, exist_ok=True)

        # Step 1: Check for an existing checkpoint
        if os.path.exists(checkpoint_path):

            logger.info("Existing checkpoint found. Loading checkpoint.")

            df_clean = pd.read_csv(
                checkpoint_path,
                dtype={
                    "InvoiceNo": "string",
                    "StockCode": "string"
                },
                parse_dates=["InvoiceDate"]
            )

        else:

            # Step 2: Extract
            df = load_excel(raw_path)

            # Step 3: Clean
            df_clean = clean_retail_data(df)

            # Step 4: Transaction features
            df_clean = create_transaction_features(df_clean)

            # Step 5: Customer features
            df_clean = create_customer_features(df_clean)

            # Step 6: Save checkpoint
            df_clean.to_csv(checkpoint_path, index=False)

            logger.info("Checkpoint saved successfully.")

        # Step 7: Validate
        validation_report = validate_retail_data(df_clean)

        print("VALIDATION REPORT")
        for check, result in validation_report.items():
            print(f"{check}: {result}")

        # Step 8: Export CSV and Parquet
        csv_path = os.path.join(
            processed_folder,
            "online_retail_features.csv"
        )

        parquet_path = os.path.join(
            processed_folder,
            "online_retail_features.parquet"
        )

        df_clean.to_csv(csv_path, index=False)

        df_clean.to_parquet(
            parquet_path,
            engine="pyarrow",
            index=False
        )

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
