import pandas as pd
import numpy as np

from abc import ABC, abstractmethod

class BasePreprocessing(ABC):
    @abstractmethod
    def transform(self, input_data):
        pass
    
class SimplePreprocessingService(BasePreprocessing):
    def transform(self, input_data):
        return input_data


class PreprocessingService(BasePreprocessing):

    FEATURE_COLUMNS = [
        "nilai_tugas",
        "nilai_uts",
        "nilai_uas",
        "rata_rata_semester_sebelumnya",
        "jumlah_mata_pelajaran_lulus",
        "jumlah_izin",
        "jumlah_sakit",
        "jumlah_alfa"
    ]

    def transform(self, input_data):
        features = self._extract_features(input_data)
        features = self._validate(features)
        return features

    def _extract_features(self, input_data):
        """
        Support:
        - dict (single row)
        - list[dict] (batch)
        - DataFrame (batch langsung)
        """

        # 1. kalau sudah DataFrame
        if isinstance(input_data, pd.DataFrame):
            df = input_data.copy()

        # 2. kalau batch list of dict
        elif isinstance(input_data, list):
            df = pd.DataFrame(input_data)

        # 3. kalau single dict
        elif isinstance(input_data, dict):
            df = pd.DataFrame([input_data])

        else:
            raise TypeError("Unsupported input type")

        # pastikan urutan kolom benar
        return df[self.FEATURE_COLUMNS]

    def _validate(self, features):
        """
        Validasi data sebelum masuk model
        """

        # cek missing value
        if features.isnull().any().any():
            raise ValueError("Input contains missing values")

        # pastikan numeric
        features = features.apply(pd.to_numeric, errors="raise")

        # clipping nilai jika diperlukan
        features = features.clip(lower=0)

        return features