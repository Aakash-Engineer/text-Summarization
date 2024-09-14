import os
import zipfile
import urllib.request as request
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.entity import DataIngestionConfig
from pathlib import Path
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            url, headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f"Downloaded file from {url} to {self.config.local_data_file}")
        else:
            logger.info(f"File already exists at {self.config.local_data_file}")

    def unzip_file(self):
        uzip_path = self.config.unzip_dir
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(uzip_path)   