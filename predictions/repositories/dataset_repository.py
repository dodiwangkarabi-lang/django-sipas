import pandas as pd
from django.conf import settings

from predictions.models import (
    Dataset, DatasetVersion
)

import hashlib

# helpers
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

class DatasetRepository:

    def __init__(self, dataset_path=None, target_column=None):
        self.dataset_path = dataset_path
        self.target_column = target_column
        self.model = Dataset
        
    def get_dataset(self, dataset_id) -> object:
        return self.model.objects.get(id=dataset_id)

    def __str__(self):
        return self.__class__.__name__
    
    def save_file(self, file) -> object:
        # simpan file ke storage
        # file = request.FILES["dataset"]

        settings.DATASET_STORAGE_DIR.mkdir(
            parents=True,
            exist_ok=True
        )
        
        # metadata
        metadata = analyze_dataset(file)

        file_path = settings.DATASET_STORAGE_DIR / file.name
        
        # simpan infomasi (metadata) ke database tabel dataset
        description = f"{file.name} - {file.size} bytes - {file.content_type}"
        dataset_obj, crated = Dataset.objects.update_or_create(
            name=file.name,
            defaults={
                "name": file.name,
                "description": description
            }
        )
        
        checksum = file_checksum(file)
        
        # cek apakah file sudah ada
        existing = DatasetVersion.objects.filter(
            dataset=dataset_obj,
            checksum=checksum
        ).first()
        
        if existing:
            dataset_version_obj = existing
        else:
            # # simpan infomasi (metadata) ke database tabel dataset_version
            dataset_version_obj, created = DatasetVersion.objects.update_or_create(
                dataset=dataset_obj,
                version="1.0",
                defaults={
                    "dataset": dataset_obj,
                    "version": "1.0",
                    "file": file,
                    "row_count": metadata["row_count"],
                    "column_count": metadata["column_count"],
                    "file_size": file.size,
                    "checksum": checksum,
                    "schema": None,
                    "preview": None,
                    "columns": metadata["columns"],
                    "target": "label",
                    "features": ["nilai_tugas", "nilai_uts", "nilai_uas", "rata_rata_semester_sebelumnya", "jumlah_mata_pelajaran_lulus", "jumlah_izin", "jumlah_sakit", "jumlah_alfa"]
                }
            )

            with open(file_path, "wb+") as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
        
        return dataset_obj

    def get_training_data(self):
        df = pd.read_csv(self.dataset_path)

        X = df.drop(columns=[self.target_column])
        y = df[self.target_column]

        return X, y