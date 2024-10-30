from sensor.logger import logging
from sensor.exception import SensorException
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.entity.config_entity import DataValidationConfig
import pandas as pd
import sys, os
from sensor.utils.main_utils import read_yaml_file, write_yaml_file
from sensor.constant.training_pipeline import SCHEMA_FILE_PATH


class DataValidation:

    def __init__(
            self,
            data_ingestion_artifact : DataIngestionArtifact, 
            data_validation_config : DataValidationConfig,
    ):
        
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise SensorException(e, sys)
        

    def is_numerical_column_exist(self,dataframe:pd.DataFrame)->bool:
        try:
            numerical_columns = self._schema_config["numerical_columns"]
            dataframe_columns = dataframe.columns

            numerical_column_present = True
            missing_numerical_columns = []
            for num_column in numerical_columns:
                if num_column not in dataframe_columns:
                    numerical_column_present=False
                    missing_numerical_columns.append(num_column)
            
            logging.info(f"Missing numerical columns: [{missing_numerical_columns}]")
            return numerical_column_present
        except Exception as e:
            raise SensorException(e,sys)
        
        
    @staticmethod
    def read_file(self, file_path) -> pd.DataFrame:

        try:
            df = pd.read_csv(file_path)
            return df
        except Exception as e:
            raise SensorException(e, sys)
        

    def validate_number_of_columns(self,dataframe:pd.DataFrame)->bool:
        try:
            number_of_columns = len(self._schema_config["columns"])
            logging.info(f"Required number of columns: {number_of_columns}")
            logging.info(f"Data frame has columns: {len(dataframe.columns)}")
            if len(dataframe.columns)==number_of_columns:
                return True
            return False
        except Exception as e:
            raise SensorException(e,sys)


    def initiate_data_validation(self):

        try:
            # get filepath from data ingestion
            train_file_path = self.data_ingestion_artifact.trainer_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            # read file from file path
            train_df = DataValidation.read_file(train_file_path)
            test_df = DataValidation.read_file(test_file_path)

            #validate number of columns
            status = self.validate_number_of_columns(train_df)
            if not status:
                error_message = f"{error_message} Train dataframe has missing columns"

            status = self.validate_number_of_columns(test_df)
            if not status:
                error_message = f"{error_message} Test dataframe has missing columns"

            status = self.is_numerical_column_exist(train_df)
            if not status:
                error_message = f"{error_message} Train dataframe has missing numerical Column"

            status = self.is_numerical_column_exist(test_df)
            if not status:
                error_message = f"{error_message} Test dataframe has missing numerical Column" 

            if len(error_message)>0:
                raise Exception(error_message)


        except Exception as e:
            raise SensorException(e, sys)

