from textSummarizer.pipeline.step1_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger

try:
    logger.info("Starting data ingestion pipeline")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info('Step 1 data ingestion completed')
except Exception as e:
    print(e)