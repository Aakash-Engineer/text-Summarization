from textSummarizer.logging import logger
from textSummarizer.pipeline.step1_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.step2_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.step3_data_transformation import DataTransformationTrainingPipeline

try:
    logger.info("Starting data ingestion pipeline")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info('Step 1 data ingestion completed')
except Exception as e:
    print(e)

try:
    logger.info("Step  data validation pipeline")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info('Step 2 data validation completed')
except Exception as e:
    print(e)

try:
    logger.info("Step  data transformation pipeline")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info('Step 3 data transformation completed')
except Exception as e:
    print(e)