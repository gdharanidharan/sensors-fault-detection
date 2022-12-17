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


class DataValidationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir: str = os.path.join( training_pipeline_config.artifact_dir, training_pipeline.DATA_VALIDATION_DIR_NAME
        ) # artifact/timestamp/data_validation

        self.valid_data_dir: str = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALIDATION_VALID_DIR
        ) # artifact/timestamp/data_validation/valid

        self.invalid_data_dir: str = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALIDATION_INVALID_DIR
        ) # artifact/timestamp/data_validation/invalid

        self.valid_train_file_path: str = os.path.join(self.valid_data_dir, training_pipeline.TRAIN_FILE_NAME
        ) # artifact/timestamp/data_validation/valid/train.csv

        self.valid_test_file_path: str = os.path.join(self.valid_data_dir, training_pipeline.TEST_FILE_NAME
        ) # artifact/timestamp/data_validation/valid/test.csv

        self.invalid_train_file_path: str = os.path.join(self.invalid_data_dir, training_pipeline.TRAIN_FILE_NAME
        ) # artifact/timestamp/data_validation/invalid/train.csv

        self.invalid_test_file_path: str = os.path.join(self.invalid_data_dir, training_pipeline.TEST_FILE_NAME
        ) # artifact/timestamp/data_validation/invalid/test.csv

        self.drift_report_file_path: str = os.path.join(
            self.data_validation_dir,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME,
        ) # artifact/timestamp/data_validation/drift_report/report.yaml


class DataTransformationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_transformation_dir: str = os.path.join( training_pipeline_config.artifact_dir,training_pipeline.DATA_TRANSFORMATION_DIR_NAME
        ) # artifact/timestamp/data_transformation

        self.transformed_train_file_path: str = os.path.join( self.data_transformation_dir,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            training_pipeline.TRAIN_FILE_NAME.replace("csv", "npy")
        ) # artifact/timestamp/data_transformation/transformed/train.npy

        self.transformed_test_file_path: str = os.path.join(self.data_transformation_dir,  training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            training_pipeline.TEST_FILE_NAME.replace("csv", "npy")
        ) # artifact/timestamp/data_transformation/transformed/test.npy

        self.transformed_object_file_path: str = os.path.join( self.data_transformation_dir, training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
            training_pipeline.PREPROCSSING_OBJECT_FILE_NAME
        ) # artifact/timestamp/data_transformation/transformed_object/preprocessing.pkl                     


class ModelTrainerConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.model_trainer_dir: str = os.path.join(
            training_pipeline_config.artifact_dir, training_pipeline.MODEL_TRAINER_DIR_NAME
        ) # artifact/timestamp/model_trainer
        
        self.trained_model_file_path: str = os.path.join(
            self.model_trainer_dir, training_pipeline.MODEL_TRAINER_TRAINED_MODEL_DIR, 
            training_pipeline.MODEL_FILE_NAME
        ) # artifact/timestamp/model_trainer/trained_model/model.pkl

        self.expected_accuracy: float = training_pipeline.MODEL_TRAINER_EXPECTED_SCORE # 0.6
        self.overfitting_underfitting_threshold = training_pipeline.MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD # 0.05

