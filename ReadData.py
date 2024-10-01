import pandas as pd
import json
import yaml
import sqlite3
import h5py
import xml.etree.ElementTree as ET
from scipy.io import loadmat

def read_data(file_path, **kwargs):
    """
    Read data from different file formats based on the file extension.
    
    Parameters:
    - file_path: Path to the file
    - kwargs: Additional parameters for pandas or other libraries (if needed)
    
    Supported formats:
    - CSV (.csv)
    - Excel (.xlsx, .xls)
    - JSON (.json)
    - YAML (.yaml, .yml)
    - XML (.xml)
    - MATLAB (.mat)
    - Parquet (.parquet)
    - HDF5 (.h5)
    - SQLite (.db)
    - Text (.txt)
    
    Returns:
    - Data read from the file, or a dictionary for non-tabular formats.
    """
    file_extension = file_path.split('.')[-1].lower()

    # Handle different file types based on extension
    if file_extension == 'csv':
        return pd.read_csv(file_path, **kwargs)
    
    elif file_extension in ['xlsx', 'xls']:
        return pd.read_excel(file_path, **kwargs)
    
    elif file_extension == 'json':
        with open(file_path, 'r') as file:
            return json.load(file)
    
    elif file_extension in ['yaml', 'yml']:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    
    elif file_extension == 'xml':
        tree = ET.parse(file_path)
        return tree.getroot()
    
    elif file_extension == 'mat':
        return loadmat(file_path)
    
    elif file_extension == 'parquet':
        return pd.read_parquet(file_path, **kwargs)
    
    elif file_extension == 'h5':
        with h5py.File(file_path, 'r') as hdf:
            return list(hdf.keys())  # Returns the list of dataset keys
    
    elif file_extension == 'db':
        conn = sqlite3.connect(file_path)
        query = kwargs.get('query', 'SELECT * FROM sqlite_master')  # Provide default query
        return pd.read_sql_query(query, conn)
    
    elif file_extension == 'txt':
        with open(file_path, 'r') as file:
            return file.read()
    
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")


def load_Data (file_path):
    data=read_data(file_path)
    print(data)