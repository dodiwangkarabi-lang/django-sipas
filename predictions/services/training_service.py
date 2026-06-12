# services/training_service.py

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from joblib import dump


from predictions.repositories.model_repository import ModelRepository
from predictions.repositories.hasil_training_repository import (
    HasilTrainingRepository
)


class TrainingService:
    def __init__(self):
        self.model_repository = ModelRepository()
        self.hasil_training_repository = HasilTrainingRepository()

    def train(
        self,
        model_name: str,
        x_train: list,
        y_train: list,
        x_test: list,
        y_test: list
    ):
        """
        Melatih model machine learning dan menghitung performanya
        menggunakan data pengujian.
        
        Args:
            model_name (str):
                Nama algoritma yang digunakan untuk training.
                Contoh: "RandomForest", "SVM".
    
            x_train (array-like):
                Data fitur yang digunakan untuk melatih model.
                Setiap baris merepresentasikan satu sampel data,
                sedangkan setiap kolom merepresentasikan fitur.
                
            y_train (array-like): 
                Label atau target yang sesuai dengan data pada x_train.
                
            x_test (array-like): 
                Data fitur yang digunakan untuk menguji model
                setelah proses training selesai.
                
            y_test (array-like): 
                Label atau target sebenarnya dari x_test yang
                digunakan untuk menghitung metrik evaluasi.

        Returns:
            ValueError: 
                Jika model_name tidak didukung.
                
        Example:
            >>> training_service.train(
            >>>     "RandomForest",
            >>>     x_train,
            >>>     y_train,
            >>>     x_test,
            >>>     y_test
            >>> )
            >>> hasil_training
        """
        model = self._build_model(model_name)

        model.fit(x_train, y_train)

        y_pred = model.predict(x_test)

        accuracy = accuracy_score(y_test, y_pred)

        model_path = (
            f"media/models/{model_name.lower()}.joblib"
        )

        self.model_repository.save_model(
            model=model,
            path=model_path
        )

        hasil_training = (
            self.hasil_training_repository.create(
                nama_model=model_name,
                akurasi=accuracy,
                lokasi_model=model_path
            )
        )

        return hasil_training

    def _build_model(self, model_name) -> object:
        models = {
            "RandomForest": RandomForestClassifier(),
            "SVM": SVC(),
        }

        if model_name not in models:
            raise ValueError(
                f"Model {model_name} tidak didukung"
            )

        return models[model_name]