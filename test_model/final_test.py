#!/usr/bin/env python3

import json
import numpy as np

from load_data import load_reviews
from feature_extractors import *
from test_classifier import compute_features

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.model_selection import cross_val_score, train_test_split, StratifiedKFold
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report



def main():
    train_data = load_reviews(folder='../data/cotraining_data/', prefix='result_data')
    test_data = load_reviews(folder='../data/', prefix='test_reviews')

#    if len(train_data['good']) > len(train_data['paid']):
#        train_data['good'] = train_data['good'][:len(train_data['paid'])]

    train_labels = [0 for i in range(len(train_data['good']))] +\
            [1 for i in range(len(train_data['paid']))]
    train_data = train_data['good'] + train_data['paid']

    print('Length of training data is {}'.format(len(train_data)))

    ground_truth_labels = [0 for i in range(len(test_data['good']))] +\
            [1 for i in range(len(test_data['paid']))]
    test_data = test_data['good'] + test_data['paid']

    print('Length of testing data is {}'.format(len(test_data)))

    words_vector = FeatureWordsVector()
    feature_words_vector = lambda x: words_vector(x, True)
    feature_funcs = [
                feature_words_vector,
                get_features_synonim,
                feature_caps_words,
                feature_contradistinctive_particles,
                feature_firstperson,
                feature_length_of_review,
                #feature_parts_of_speech,
                feature_unigrams_bigrams,
                get_features_mean_len_word,
                get_features_meta,
                get_features_number_exclamation,
            ]

    train_data_features = compute_features(train_data, feature_funcs) 

    feature_words_vector = lambda x: words_vector(x, False)
    feature_funcs = [
                feature_words_vector,
                get_features_synonim,
                feature_caps_words,
                feature_contradistinctive_particles,
                feature_firstperson,
                feature_length_of_review,
                #feature_parts_of_speech,
                feature_unigrams_bigrams,
                get_features_mean_len_word,
                get_features_meta,
                get_features_number_exclamation,
            ]

    test_data_features = compute_features(test_data, feature_funcs)

    clf = RandomForestClassifier(n_estimators=500, n_jobs=-1, random_state=42)
    clf.fit(train_data_features, train_labels)
    
    predicted_labels = clf.predict(test_data_features)

    print(predicted_labels)
    print(ground_truth_labels)

    print('Accuracy score:', accuracy_score(ground_truth_labels, predicted_labels))


if __name__ == '__main__':
    main()
