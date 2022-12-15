from datetime import datetime
import os
from sensor.constant  import training_pipeline

class TrainingPipelineConfig:

    def __init__(self,timestamp=datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")                              # timestamp
        self.pipeline_name: str = training_pipeline.PIPELINE_NAME                        # sensor
        self.artifact_dir: str = os.path.join(training_pipeline.ARTIFACT_DIR, timestamp) # artifact/timestamp
        self.timestamp: str = timestamp


class DataIngestionConfig:
        def __init__(self,training_pipeline_config:TrainingPipelineConfig):
            self.data_ingestion_dir: str = os.path.join(
                training_pipeline_config.artifact_dir, training_pipeline.DATA_INGESTION_DIR_NAME 
            ) # artifact/timestamp/data_ingestion

            self.feature_store_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.FILE_NAME
            ) # artifact/timestamp/data_ingestion/feature_store/sensor.csv

            self.training_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TRAIN_FILE_NAME
            ) # artifact/timestamp/data_ingestion/ingested/train.csv

            self.testing_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TEST_FILE_NAME
            ) # artifact/timestamp/data_ingestion/ingested/test.csv

            self.train_test_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION # 0.2
            self.collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME # sensor

