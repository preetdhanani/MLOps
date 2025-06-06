from mlProject import logger
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation
from mlProject.components.data_transformation import DataTransformation


STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open("artifacts/data_validation/status.txt", 'r') as file:
                status = file.read().split(" ")[-1]    
            if status != "True":
                raise Exception("Data validation failed. Cannot proceed with data transformation.")
            else:
                config = ConfigurationManager()
                data_transformation_config = config.data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
        except Exception as e:
            logger.exception(e)
            raise e
        

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

    