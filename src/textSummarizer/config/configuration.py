from textSummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from textSummarizer.utils.common import read_yaml, create_dirs
from textSummarizer.entity import DataIngestionConfig
class ConfigurationManager:
    def __init__(
            self, 
            config_file_path = CONFIG_FILE_PATH,
            params_file_path =  PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        create_dirs([self.config.artifacts_root])

    def data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config.data_ingestion

        create_dirs([config.root_dir])
        
        return DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )