# services/model_selection_service.py

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier


class ModelSelectionService:

    def get_model(self, model_name):
        models = {
            "random_forest": RandomForestClassifier(
                n_estimators=100,
                random_state=42
            ),
            "svm": SVC(
                kernel="rbf",
                probability=True
            ),
            "decision_tree": DecisionTreeClassifier(
                random_state=42
            ),
            "knn": KNeighborsClassifier(
                n_neighbors=5
            ),
        }

        model = models.get(model_name)

        if model is None:
            raise ValueError(
                f"Model '{model_name}' tidak didukung."
            )

        return model