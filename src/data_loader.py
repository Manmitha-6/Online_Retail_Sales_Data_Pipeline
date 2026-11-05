
import pandas as pd
import logging

logger = logging.getLogger(__name__)


def load_excel(file_path):
    """
    Load the raw retail dataset from an Excel file.
    """
    try:
        logger.info("Loading Excel file: %s", file_path)

        df = pd.read_excel(file_path, engine="calamine")

        logger.info("Excel dataset loaded successfully. Shape: %s", df.shape)

        return df

    except Exception:
        logger.exception("Error while loading Excel dataset.")
        raise


def load_csv(file_path):
    """
    Load a retail dataset from a CSV file.
    """
    try:
        logger.info("Loading CSV file: %s", file_path)

        df = pd.read_csv(file_path)

        logger.info("CSV dataset loaded successfully. Shape: %s", df.shape)

        return df

    except Exception:
        logger.exception("Error while loading CSV dataset.")
        raise
