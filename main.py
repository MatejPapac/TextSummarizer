from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_2_data_transformation_pipeline import DataTransformationPipeline
from src.textSummarizer.pipeline.stage_3_model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.textSummarizer.pipeline.stage_4_model_evaluation import ModelEvaluationTrainingPipeline
STAGE_NAME="Data ingestion stage"

try:
    logger.info(f'stage{STAGE_NAME} initiated')
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Transformation stage"

try:
    logger.info(f'stage{STAGE_NAME} initiated')
    data_ingestion_pipeline=DataTransformationPipeline()
    data_ingestion_pipeline.initiate_data_transformation()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model training stage"

try:
    logger.info(f'stage{STAGE_NAME} initiated')
    data_ingestion_pipeline=ModelTrainerTrainingPipeline()
    data_ingestion_pipeline.initiate_model_trainer()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Evaluation stage"

try:
    logger.info(f'stage{STAGE_NAME} initiated')
    data_ingestion_pipeline=ModelEvaluationTrainingPipeline()
    data_ingestion_pipeline.initiate_model_evaluation()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e
