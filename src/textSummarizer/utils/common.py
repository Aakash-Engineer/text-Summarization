import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from pathlib import Path


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a yaml file and return a ConfigBox object
    :param path_to_yaml: Path to yaml file
    :return: ConfigBox object
    """
    try:
        with open(path_to_yaml, 'r') as file:
            content = yaml.safe_load(file)
            logger.info(f"Read yaml file from {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        logger.error("Error reading yaml file")
        raise BoxValueError('Error reading yaml file')
    except Exception as e:
        raise e
    
@ensure_annotations
def create_dirs(path_to_dir: list, verbose=True):
    """
    Create directories if they do not exist
    :param path_to_dir: List of directories to create
    :param verbose: ignore log (bool, optional)
    """

    for path in path_to_dir:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory {path}")

@ensure_annotations
def get_size(path_to_file: Path) -> str:
    """
    Get the size of a file
    :param path_to_file: Path to file
    :return: Size of file
    """
    size = os.path.getsize(path_to_file)
    return size