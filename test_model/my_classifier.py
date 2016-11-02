import random

class RandomClassifier:
    def __init__(self):
        pass

    def fit(self, X, y):
        pass

    def predict(self, X):
        return [random.randint(0, 1) for i in range(len(X))]

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
