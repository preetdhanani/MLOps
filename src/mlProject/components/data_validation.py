from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd
import os

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self)-> bool:
        try:
            validation_status = True

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_scheme = self.config.all_scheme.keys()

            for col in all_cols:
                if col not in all_scheme:
                    validation_status = False
                    break  # stop checking further, as validation already failed

            if os.path.exists(self.config.STATUS_FILE):
                os.remove(self.config.STATUS_FILE)
                logger.info(f"Existing file deleted.")

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e

        
