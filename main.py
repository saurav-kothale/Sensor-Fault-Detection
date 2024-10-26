from sensor.configuration.mongodb_configuration import MongoDBClient
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig

if __name__ == "__main__":

    training_pipeline_config = TrainingPipelineConfig()

    data_ingestion_cofig = DataIngestionConfig(training_pipeline_config)

    print(data_ingestion_cofig.__dict__)
    
    
