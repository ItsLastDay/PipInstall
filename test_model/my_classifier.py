from sklearn.ensemble import RandomForestClassifier

class Classifier:
    def __init__(self):
        self.cls = RandomForestClassifier(n_estimators=30)

    def fit(self, X, y):
        self.cls.fit(X, y)

    def predict(self, X):
        return self.cls.predict(X)


def get_features_inner(reviews_array):
    features = []
    for review in reviews_array:
        features.append([0, 1, 4, 0])

    return features


def get_features(reviews_dict):
    features = get_features_inner(reviews_dict['good'])
    features.extend(get_features_inner(reviews_dict['paid']))

    labels = [0 for i in range(len(reviews_dict['good']))]
    labels.extend([1 for i in range(len(reviews_dict['paid']))])

    return features, labels
