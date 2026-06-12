class FeatureService:

    def __init__(self, feature_columns):
        self.feature_columns = feature_columns

    def transform(self, dataframe):
        return dataframe[self.feature_columns]
    
# pemakaian
# feature_columns = [
#     "nilai_tugas",
#     "nilai_uts",
#     "nilai_uas",
# ]

# service = FeatureService(feature_columns)
# features = service.transform(dataframe)