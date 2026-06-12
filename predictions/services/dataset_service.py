from django.core.files.base import ContentFile
from io import BytesIO
import joblib

# repository
from predictions.repositories.dataset_repository import DatasetRepository
from predictions.repositories.training_run_repository import TrainingRunRepository
from predictions.repositories.model_repository import ModelRepository

# services
from predictions.services.model_trainer import ModelTrainer

# models
from predictions.models import (
    ModelML
)

import pandas as pd

class DatasetService:
    def __init__(self):
        self.dataset_repository = DatasetRepository()
        self.training_run_repository = TrainingRunRepository()
        self.model_repository = ModelRepository()
        
    def create_dataset(self, file, metadata: dict=None):
        dataset = self.dataset_repository.save_file(file)
        
        return dataset
    
    def _extract_features(self, input_data, features: list, target: str):
        """
        extract features

        Args:
            input_data (DataFrame): pandas DataFrame of dataset version
            
        Returns:
            X, y
        """
        X = input_data[features]
        y = input_data[target]
        
        return X, y
    
    def train_model(self, dataset_id):
        """
        melatih model

        Args:
            dataset_id (str | int): id dari dataset (model Dataset)

        Returns:
            (model, metrics): model dan metrics
        """
        dataset = self.dataset_repository.get_dataset(dataset_id)
        dataset_version = dataset.active_version
        dataset_file = dataset.active_version.file 
        dataset_df = pd.read_csv(dataset_file)
        
        # latih model
        model_trainer = ModelTrainer()
        X, y = self._extract_features(dataset_df, features=dataset_version.features, target=dataset_version.target)
        test_size = 0.2
        random_state = 42
        X_train, X_test, y_train, y_test = model_trainer.train_test_split(X, y, test_size=test_size, random_state=random_state)
        
        # print(X_train, X_test)
        # print(y_train, y_test)
        
        # dataset_metadata
        dataset_metadata = {
            "train_size": len(X_train),
            "test_size": len(X_test),
            "feature_count": len(dataset_version.features),
            "target_column": dataset_version.target,
            "test_ratio": test_size,
            "random_state": random_state
        }
        
        model_trainer.train(X_train, y_train) # melatih model
        metrics = model_trainer.evaluate_model(X_test, y_test) # melakukan evaluasi model
        
        # simpan metrics dan lainnya di database tabel training run (model TrainingRunRepository)
        training_run_obj, created = self.training_run_repository.update_or_create(
            dataset_version_obj=dataset_version, 
            metrics=metrics,
            algorithm="Random Forest Classifier",
            dataset_version=dataset_version,
            hyperparameters=model_trainer._params,
            dataset_metadata=dataset_metadata
        )
        
        model = model_trainer.get_model()
        
        # ============= simpan model ke database =================
        buffer = BytesIO()
        # simpan model ke buffer (bukan file disk)
        joblib.dump(model, buffer)
        buffer.seek(0)
        
        # convert ke Django File
        file_model = ContentFile(buffer.read())
        file_model.name = "model.joblib"
        file_model.size = buffer.getbuffer().nbytes
        # atribut custom
        file_model.content_type = "application/octet-stream"
        
        # simpan model ke database
        self.model_repository.save_ke_db(
            training_run=training_run_obj,
            nama="Random Forest Classifier",
            file_model=file_model
            # checksum=model_trainer._checksum
        )
        
        
        
        return model, metrics
        # return (1, 2)