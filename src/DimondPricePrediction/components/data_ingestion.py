import pandas as pd
import numpy as np
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception

import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path


#configuration of data
class DtatIngestionConfig:
    raw_data_path:str=os.path.join('artifacts','raw.csv')
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')



class DataIngestion:
    def __init__(self):
        # obj od dataingestionconfig to acess data paths
        self.ingestion_config=DtatIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("data ingestion started")

        try:
            data=pd.read_csv(Path(os.path.join('notebooks/data','gemstone.csv')))
            logging.info('I have resd the dataset as df')
            
#           making of dir,dir name i.e artifacts,path join of raw data and dir
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True) #dir
            data.to_csv(self.ingestion_config.raw_data_path,index=False)    # save data into csv for
            logging.info('I have save data in artifact folder')

            logging.info('perform train test split')
            
            train_data,test_data=train_test_split(data,test_size=0.25)
            logging.info('train test split complited')

            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)

            logging.info('data ingestion part completed')
            return (
                 
                
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
        except Exception as e:
           logging.info("exception during occured at data ingestion stage")
           raise customexception(e,sys)
    