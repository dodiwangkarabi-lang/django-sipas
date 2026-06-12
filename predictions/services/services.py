import joblib
from pathlib import Path

class ModelService:
    def load_model(self, file_path):
        """

        Args:
            file_path (_type_): _description_

        Returns:
            _type_: _description_
            
        Example:
        
            service = ModelService()

            model = service.load_model(
                "models/rf_v1.joblib"
            )

            hasil = model.predict(data_baru)
        """
        return joblib.load(file_path)
    
    def save_model(self, model, filename):
        model_dir = Path("models")
        model_dir.mkdir(exist_ok=True)

        file_path = model_dir / f"{filename}.joblib"

        joblib.dump(model, file_path)

        return str(file_path)

# Contoh Penggunaan
# service = ModelService()

# file_path = service.save_model(
#     model=random_forest_model,
#     filename="rf_v1"
# )

# print(file_path)
# models/rf_v1.joblib