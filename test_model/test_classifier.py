#!/usr/bin/env python3

from sklearn.model_selection import StratifiedKFold
from sklearn import metrics
import numpy as np

from load_data import load_reviews
from my_classifier import get_features, Classifier

if __name__ == '__main__':
    # Load reviews as dict with two keys: 'good' and 'paid'.
    reviews = load_reviews()

    # Preprocess all reviews, return two arrays if length n:
    # 1. vector of features for each object,
    # 2. label for each object (0 - good, 1 - paid).
    features, labels = get_features(reviews)    
    features = np.array(features)
    labels = np.array(labels)

    it = 0
    mean_score = 0
    skf = StratifiedKFold(n_splits=10)
    for train, test in skf.split(features, labels):
        train_features, train_labels = features[train], labels[train]
        test_features, test_labels = features[test], labels[test]

        cls = Classifier()
        cls.fit(train_features, train_labels)

        predicted_labels = cls.predict(test_features)
        
        score = metrics.f1_score(test_labels, predicted_labels)
        mean_score += score
        it += 1
        print('Score on iteration {} is: {}'.format(it, score))

    mean_score /= it
    print('Mean overall score is: {}'.format(mean_score))

