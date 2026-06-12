import hashlib

import pandas as pd

def file_checksum(file):
    sha = hashlib.sha256()
    for chunk in file.chunks():
        sha.update(chunk)
    return sha.hexdigest()

def analyze_dataset(file):
    """
    Return metadata: rows, columns, column names
    """

    # reset pointer file (penting untuk uploaded file)
    file.seek(0)

    if file.name.endswith(".csv"):
        df = pd.read_csv(file)
    elif file.name.endswith(".xlsx"):
        df = pd.read_excel(file)
    else:
        raise ValueError("Unsupported file type")

    metadata = {
        "row_count": len(df),
        "column_count": len(df.columns),
        "columns": list(df.columns),
    }

    return metadata