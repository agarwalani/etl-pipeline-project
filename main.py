import logging
from extract.extract_api import fetch_data
from transform.transform import transform_data
from load.load import load_data

logging.basicConfig(
    filename='logs/etl.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_pipeline():
    try:
        logging.info("ETL Started")
        print("ETL Started")
        data = fetch_data()
        logging.info("Data Extracted")
        print("Data Extracted")

        df = transform_data(data)
        logging.info("Data Transformed")
        print("Data Transformed")

        load_data(df)
        logging.info("Data Loaded")
        print("Data Loaded")

        logging.info("ETL Completed Successfully")

        print("ETL Completed")
    
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    run_pipeline()