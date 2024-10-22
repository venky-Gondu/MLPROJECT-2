import os
import sys
from srs.exception import CustomException
from srs.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from srs.components.data_transformation import DataTransformation
from srs.components.data_transformation import DataTransformationConfig
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebooks/data/stud.csv')  # Ensure this path is correct
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    try:
        obj = DataIngestion()
        train_data_path, test_data_path = obj.initiate_data_ingestion()
        print(f"Train data saved to: {train_data_path}")
        print(f"Test data saved to: {test_data_path}")
    except CustomException as e:
        logging.error(f"An error occurred: {e}")
        print(e)
    data_transformation=DataTransformation()
    data_transformation.initiate_data_transformation(train_data_path,test_data_path)
