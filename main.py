from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationPipeline

STAGE_NAME1 = "Data Ingestion stage"
STAGE_NAME2 = "Data Valifation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME1} started <<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME1} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


try:
    logger.info(f">>>>>> stage {STAGE_NAME2} started <<<<<<")
    obj = DataValidationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME2} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e