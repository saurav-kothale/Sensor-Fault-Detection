from sensor.configuration.mongodb_configuration import MongoDBClient
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
# from sensor.pipeline import training_pipeline
from sensor.pipeline.training_pipeline import TrainingPipeline

if __name__ == "__main__":

    training_pipeline = TrainingPipeline()
    training_pipeline.run_pipeline()

    
    
