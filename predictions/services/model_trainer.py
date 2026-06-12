from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report
)

# train split
from sklearn.model_selection import train_test_split

class ModelTrainer:
    
    def __init__(self):
        self._model = RandomForestClassifier
        self._params = {"n_estimators": 100, "random_state": 42}
        
    def get_model(self):
        return self._model
        
    def train_test_split(self, X, y, test_size=0.2, random_state=42, **kwargs):
        return train_test_split(
            X,
            y, 
            test_size=test_size,
            random_state=random_state,
            **kwargs
        )

    def __str__(self):
        return self.__class__.__name__
    
    def set_model(self, model):
        self._model = model
        
    def set_params(self, params: dict):
        """
        metode ini digunakan untuk mengatur parameter pada model
        
        Args:
            params (dict): 
                parameter yang digunakan untuk melatih model
        
        Example:
            
            trainer = ModelTrainer()
            trainer.set_params({"n_estimators": 100, "random_state": 42})
        """
        self._params = params

    def train(self, X, y):
        model = RandomForestClassifier(
            # n_estimators=100,
            # random_state=42
            **self._params
        )
        
        model.fit(X, y)
        
        self._model = model
        return self._model
        
        
        
        # self._model(**self._params)
        
        # print("type", type(self._model))

        # self._model.fit(X, y)

        # return self._model
    
    def evaluate_model(self, X_test, y_test) -> dict:
        y_pred = self._model.predict(X_test)

        metrics = {
            "accuracy": accuracy_score(y_test, y_pred),
            "precision": precision_score(y_test, y_pred, average="weighted", zero_division=0),
            "recall": recall_score(y_test, y_pred, average="weighted", zero_division=0),
            "f1_score": f1_score(y_test, y_pred, average="weighted", zero_division=0),
            "report": classification_report(y_test, y_pred, zero_division=0, output_dict=True)
        }

        return metrics