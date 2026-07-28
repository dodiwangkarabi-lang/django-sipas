from django.conf import settings

from academics.models import (
    Siswa
)

# repositories
from predictions.repositories.dataset_repository import DatasetRepository

# services
from predictions.services.data_builder_service import DataBuilderService
from predictions.services.feature_service import FeatureService
from predictions.services.prediction_service import PredictionService
from predictions.services.model_trainer import ModelTrainer
from predictions.services.dataset_service import DatasetService


# repositories
from predictions.repositories.model_repository import ModelRepository

# constants
from predictions.constants.constants import (
    FEATURE_COLUMNS
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)


class EvaluasiModelFacade:

    @staticmethod
    def evaluate(model, x_test, y_test):

        y_pred = model.predict(x_test)

        return {
            "accuracy": accuracy_score(y_test, y_pred),
            "precision": precision_score(
                y_test,
                y_pred,
                average="weighted",
                zero_division=0,
            ),
            "recall": recall_score(
                y_test,
                y_pred,
                average="weighted",
                zero_division=0,
            ),
            "f1_score": f1_score(
                y_test,
                y_pred,
                average="weighted",
                zero_division=0,
            ),
        }
        
class UploadDatasetFacade:
    @staticmethod
    def execute(file=None, metadata: dict=None):
        """
        upload dataset

        Args:
            file (_type_, optional): request.FILES["dataset"]. Defaults to None.
            metadata (dict, optional): _description_. Defaults to None.
        """
        dataset_service = DatasetService()
        # hapus semua dataset
        # dataset_service.delete_all_dataset()
        # hapus semua model
        # dataset_service.delete_all_model()
        dataset = dataset_service.create_dataset(file, metadata)
        model, metrics = dataset_service.train_model(dataset_id=dataset.id)
        
        return (model, metrics)
        

class LatihModelFacade:
    @staticmethod
    def latih(dataset: None | str = None) -> object:
        if dataset is None:
            dataset = settings.DATASET_STORAGE_DIR / "dataset.csv"
            
        data_repository = DatasetRepository(dataset_path=dataset, target_column="label")
        X, y = data_repository.get_training_data()
        model_trainer = ModelTrainer()
        model = model_trainer.train(X, y)
        
        return model
    
class SimpanModelFacade:
    @staticmethod
    def simpan(model, model_path=None):
        model_repository = ModelRepository(model_path=model_path or "model.joblib")
        model_repository.save(model)
        
        return model_repository

class AdminPredictionFacade:
    @staticmethod
    def prediksi(*, siswa_id, model_id=None) -> list:
        if model_id is None:
            raise ValueError("model_id is required")
        
        siswa = Siswa.objects.get(id=siswa_id)
        data_builder_service = DataBuilderService()
        siswa_df = data_builder_service.build(siswa)
        
        feature_service = FeatureService(FEATURE_COLUMNS)
        # features = feature_service.transform(siswa_df)
        
        # model_repository = ModelRepository("model.joblib")
        nama_model = ModelRepository().load_model_db(model_id).file_model.name
        model_repository = ModelRepository(model_path=nama_model)
        prediction_service = PredictionService(
            model_repository=model_repository, preprocessing_service=feature_service
        )
        hasil_prediksi = prediction_service.predict(siswa_df)
        
        return hasil_prediksi