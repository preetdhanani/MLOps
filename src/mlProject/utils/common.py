import os
from pathlib import Path
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: str) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (str): Path to the YAML file.
        
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)

            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty.")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories from a list of paths.

    Args:
        path_to_directories (list): List of paths to create directories.
        verbose (bool, optional): Whether to print log messages. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: str, data: dict):
    """
    Saves a dictionary as a JSON file.

    Args:
        path (str): Path to save the JSON file.
        data (dict): Dictionary to be saved as JSON.
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)

    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: str) -> ConfigBox:
    """
    Loads a JSON file and returns its content as a ConfigBox object.

    Args:
        path (str): Path to the JSON file.

    Returns:
        ConfigBox: Content of the JSON file as a ConfigBox object.
    """
    with open(path) as json_file:
        content = json.load(json_file)

    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content) 

@ensure_annotations 
def load_bin(path: Path) -> Any:
    """
    Loads a binary file using joblib.

    Args:
        path (str): Path to the binary file.

    Returns:
        Any: Content of the binary file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return ConfigBox(data)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves data as a binary file using joblib.

    Args:
        data (Any): Data to be saved.
        path (str): Path to save the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of a file or directory in a human-readable format.

    Args:
        path (Path): Path to the file or directory.

    Returns:
        str: Size of the file or directory in a human-readable format.
    """
    size = os.path.getsize(path)
    return f"{size / (1024 * 1024):.2f} MB" if size > 0 else "0 MB"