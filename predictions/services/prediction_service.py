# services/prediction_service.py

from predictions.repositories.model_repository import (
    ModelRepository
)
from predictions.repositories.hasil_training_repository import (
    HasilTrainingRepository
)
from predictions.repositories.hasil_prediksi_repository import (
    HasilPrediksiRepository
)



# class PredictionService:

#     def __init__(self):
#         self.model_repository = ModelRepository()
#         self.hasil_prediksi_repository = (
#             HasilPrediksiRepository()
#         )
        
#     def set_model_repository(self, model_repository):
#         self.model_repository = model_repository

#     def predict(
#         self,
#         model_path,
#         features,
#         save=False
#     ):
#         """
#         Melakukan prediksi menggunakan model yang telah ditraining

#         Args:
#             model_path (str): 
#                 Path file model
#             features (array-like): 
#                 Data fitur yang digunakan untuk menguji model

#         Returns:
#             _type_: _description_
            
#         Example:
            
#             service = PredictionService()

#             hasil_prediksi = service.predict(
#                 "models/rf_v1.joblib",
#                 data_baru
#             )
#         """
#         model = self.model_repository.load_model(
#             model_path
#         )

#         prediction = model.predict(
#             features
#         )
        
#         # if save:
#         #     self.hasil_prediksi_repository.create(
#         #         hasil=str(prediction)
#         #     )

#         hasil_prediksi = prediction

#         return hasil_prediksi

class PredictionService:

    def __init__(
        self,
        model_repository,
        preprocessing_service
    ):
        self.model_repository = model_repository
        self.preprocessing_service = preprocessing_service

    def predict(self, input_data):
        model = self.model_repository.load()
        features = self._build_features(input_data)
        return model.predict(features)
    
    def _build_features(self, input_data):
        return self.preprocessing_service.transform(input_data)

    def validate_input(self, input_data):
        pass

    def preprocess_input(self, input_data):
        pass

    def load_model(self):
        pass