# services/testing_service.py

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

from predictions.repositories.model_repository import (
    ModelRepository
)


class TestingService:

    def __init__(self):
        self.model_repository = ModelRepository()

    def test(
        self,
        model_path,
        x_test,
        y_test
    ):
        model = self.model_repository.load_model(
            model_path
        )

        predictions = model.predict(x_test)

        return {
            "accuracy": accuracy_score(
                y_test,
                predictions
            ),
            "precision": precision_score(
                y_test,
                predictions,
                average="weighted"
            ),
            "recall": recall_score(
                y_test,
                predictions,
                average="weighted"
            ),
            "f1_score": f1_score(
                y_test,
                predictions,
                average="weighted"
            ),
        }