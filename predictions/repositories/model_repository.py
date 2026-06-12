# repositories/model_repository.py

from pathlib import Path
from django.conf import settings

from joblib import dump, load

# models
from predictions.models import (
    ModelML, TrainingRun, DatasetVersion
)

# utils
from .utils.utils import analyze_dataset, file_checksum

class ModelRepository:
    
    def __init__(self, model_path=None):
        self._model_path = model_path
        self._model = None
        
    def load_model_db(self, model_id):
        return ModelML.objects.get(id=model_id)
        
    def load(self) -> object:
        if self._model is None:
            self._model = self.load_model(self._model_path)
        return self._model
    
    def save(self, model):
        if self._model_path is None:
            raise ValueError("Model path is not set")
        
        model_dir = settings.MODEL_STORAGE_DIR
        model_dir.mkdir(exist_ok=True)

        path = model_dir / self._model_path

        dump(model, path)

        return path
    
    def save_ke_db(self, **kwargs):

        settings.MODEL_STORAGE_DIR.mkdir(
            parents=True,
            exist_ok=True
        )
        
        # fields ModelML
        training_run = kwargs["training_run"]
        nama = kwargs["nama"]
        file_model = kwargs["file_model"]
        # checksum = kwargs["checksum"]
        
        # initial
        file = kwargs["file_model"]
        training_run_obj = training_run
        
        # metadata
        # metadata = analyze_dataset(file)

        file_path = settings.MODEL_STORAGE_DIR / file.name
        
        # simpan infomasi (metadata) ke database tabel dataset
        # description = f"{file.name} - {file.size} bytes - {file.content_type}"
        # dataset_obj, crated = ModelML.objects.update_or_create(
        #     name=file.name,
        #     defaults={
        #         "name": file.name,
        #         "description": description
        #     }
        # )
        
        checksum = file_checksum(file)
        
        # cek apakah file sudah ada
        existing = ModelML.objects.filter(
            training_run=training_run_obj,
            checksum=checksum
        ).first()
        
        if existing:
            obj = existing
        else:
            # # simpan infomasi (metadata) ke database tabel dataset_version
            obj, created = ModelML.objects.update_or_create(
                training_run=training_run_obj,
                nama = nama,
                defaults={
                    "training_run": training_run_obj,
                    "file_model": file_model,
                    "checksum": checksum,
                    "nama": nama
                }
            )
        
        return obj
        
    
    def load_model(self, file_name) -> object:
        model_path = (
            Path(settings.MODEL_STORAGE_DIR)
            / file_name
        )

        return load(model_path)

    # def save_model(self, model, path):
    #     dump(model, path)

    # def load_model(self, path):
    #     return load(path)