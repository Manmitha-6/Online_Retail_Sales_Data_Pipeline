
import os
import logging
import yaml
import pandas as pd

from data_loader import load_excel
from data_cleaning import clean_retail_data
from feature_engineering import (
    create_transaction_features,
    create_customer_features
)
from validation import validate_retail_data


# --------------------------------------------------
# 1. Load YAML Configuration
# --------------------------------------------------

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

CONFIG_PATH = os.path.join(
    PROJECT_ROOT, "config", "config.yaml"
)

with open(CONFIG_PATH, "r", encoding="utf-8") as file:
    CONFIG = yaml.safe_load(file)


def project_path(path):
    return os.path.join(PROJECT_ROOT, path)


# --------------------------------------------------
# 2. Configure Logging
# --------------------------------------------------

LOG_FOLDER = project_path(CONFIG["paths"]["log_dir"])
os.makedirs(LOG_FOLDER, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(
        LOG_FOLDER,
        CONFIG["logging"]["filename"]
    ),
    level=getattr(logging, CONFIG["logging"]["level"].upper()),
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

logger = logging.getLogger(__name__)


# --------------------------------------------------
# 3. Main ETL Pipeline
# --------------------------------------------------

def run_pipeline(
    raw_path=None,
    checkpoint_path=None,
    processed_folder=None
):

    try:
        logger.info("Retail data pipeline started.")

        raw_path = raw_path or project_path(
            CONFIG["paths"]["raw_data"]
        )

        checkpoint_path = checkpoint_path or project_path(
            CONFIG["paths"]["checkpoint"]
        )

        processed_folder = processed_folder or project_path(
            CONFIG["paths"]["processed_dir"]
        )

        os.makedirs(os.path.dirname(checkpoint_path), exist_ok=True)
        os.makedirs(processed_folder, exist_ok=True)

        # Step 1: Load checkpoint or execute ETL

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

            logger.info("Extracting Excel dataset.")
            df = load_excel(raw_path)

            # Step 3: Clean

            logger.info("Cleaning transaction data.")
            df_clean = clean_retail_data(df)

            # Step 4: Transaction features

            logger.info("Generating transaction features.")
            df_clean = create_transaction_features(df_clean)

            # Step 5: Customer features

            logger.info("Generating customer features.")
            df_clean = create_customer_features(df_clean)

            df_clean["InvoiceNo"] = df_clean["InvoiceNo"].astype("string")
            df_clean["StockCode"] = df_clean["StockCode"].astype("string")

            # Step 6: Save checkpoint

            df_clean.to_csv(checkpoint_path, index=False)

            logger.info("Checkpoint saved successfully.")

        df_clean["InvoiceNo"] = df_clean["InvoiceNo"].astype("string")
        df_clean["StockCode"] = df_clean["StockCode"].astype("string")

        # Step 7: Validate

        logger.info("Validating processed dataset.")

        validation_report = validate_retail_data(df_clean)

        print("\nFINAL VALIDATION REPORT")

        for check, result in validation_report.items():
            print(f"{check}: {result}")

        # Step 8: Export CSV and Parquet

        csv_path = os.path.join(
            processed_folder,
            CONFIG["output"]["csv_filename"]
        )

        parquet_path = os.path.join(
            processed_folder,
            CONFIG["output"]["parquet_filename"]
        )

        df_clean.to_csv(csv_path, index=False)

        df_clean.to_parquet(
            parquet_path,
            engine="pyarrow",
            index=False
        )

        logger.info("CSV and Parquet exports completed.")
        logger.info("Pipeline completed successfully.")

        print("\nPIPELINE COMPLETED SUCCESSFULLY!")
        print("Final dataset shape:", df_clean.shape)
        print("CSV saved at:", csv_path)
        print("Parquet saved at:", parquet_path)

        return df_clean

    except Exception:
        logger.exception("Retail data pipeline failed.")
        raise


if __name__ == "__main__":
    run_pipeline()
