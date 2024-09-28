
common_data_file_types = [
    # Text-Based Formats
    '.csv',   # Comma-Separated Values
    '.tsv',   # Tab-Separated Values
    '.txt',   # Plain Text
    '.json',  # JavaScript Object Notation
    '.xml',   # eXtensible Markup Language
    '.yaml',  # YAML Ain't Markup Language

    # Spreadsheet Formats
    '.xlsx',  # Excel Workbook
    '.xls',   # Excel 97-2003 Workbook
    '.xlsm',  # Excel Macro-Enabled Workbook

    # Database Formats
    '.sql',   # Structured Query Language Dump
    '.sqlite',# SQLite Database
    '.db',    # Generic Database File
    '.accdb', # Microsoft Access Database
    '.mdb',   # Microsoft Access Database (older version)
    
    # Binary Formats
    '.parquet', # Parquet
    '.avro',    # Avro
    '.orc',     # Optimized Row Columnar

    # Specialized Formats
    '.h5',      # HDF5
    '.hdf5',    # HDF5
    '.mat',     # MATLAB Data File
    '.nc'       # Network Common Data Form
]

common_config_file_types = [
    '.ini',      # INI File
    '.json',     # JSON File
    '.yaml',     # YAML File
    '.yml',      # YAML File (alternative extension)
    '.xml',      # XML File
    '.toml',     # TOML File
    '.properties' # Properties File
]

def validate_data_file_type(input_string):
    
    parts = input_string.rsplit('.', 1)
    
    # Get the last part
    last_part = parts[-1] if len(parts) > 1 else input_string
    
    # Check if the last part matches any of the file types
    if f'.{last_part}' in common_data_file_types:
        return True
    else:
        return False

def validate_config_file_type(input_string):
    
    parts = input_string.rsplit('.', 1)
    
    # Get the last part
    last_part = parts[-1] if len(parts) > 1 else input_string
    
    # Check if the last part matches any of the file types
    if f'.{last_part}' in common_config_file_types:
        return True
    else:
        return False