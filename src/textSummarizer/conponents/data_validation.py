import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig) -> None:
        self.config = config
    
    def chech_status_file(self):
        try:
            validation_sataus = None
            all_files = os.listdir(os.path.join('artifacts', 'data_ingestion', 'samsum_dataset'))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_sataus = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'{validation_sataus}')
                else:
                    validation_sataus = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'{validation_sataus}')
                                                
            return validation_sataus
        except Exception as e:
            raise e