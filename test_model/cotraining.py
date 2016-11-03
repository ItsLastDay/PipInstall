#!/usr/bin/env python3

import json
import numpy

from load_data import load_reviews
from feature_extractors import *
from test_classifier import compute_features

import sklearn.naive_bayes

MIN_PROBA = 0.9
COTRAIN_FOLDER = '../data/cotraining_data'

if __name__ == '__main__':
    seed_data = load_reivews(folder=COTRAIN_FOLDER, prefix='seed')

    raw_data = json.load('{}/raw_data.json'.format(COTRAIN_FOLDER))
    # Only results with grade >= 4 (which is >= 1 in -2..2). 
    raw_data = list(filter(lambda x: x['grade'] >= 1, raw_data))
    raw_data = np.array(raw_data)

    cur_data_good = np.array(seed_data['good'])
    cur_data_paid = np.array(seed_data['paid'])

    while True:
        cls_review_centric = sklearn.naive_bayes.MultinomialNB()
        cls_user_centric = sklearn.naive_bayes.GaussianNB()

        flat_reviews = cur_data_good + cur_data_paid
        labels = [0 for i in range(len(cur_data_good))] +\
                [1 for i in range(len(cur_data_paid))]

        words_vector = FeatureWordsVector()
        feature_words_vector = lambda x: words_vector(x, True)

        # Train two classifiers on distinc features.
        train_features_review_centric = compute_features(flat_reviews,
                [feature_words_vector, feature_mean_len_word,
                    feature_parts_of_speech])
        train_features_user_centric = compute_features(flat_reviews,
                [feature_meta])

        cls_review_centric.fit(train_features_review_centric, labels)
        cls_user_centric.fit(train_features_user_centric, labels)


        # Get features for raw data.
        feature_words_vector = lambda x: words_vector(x, False)
        test_features_review_centric = compute_features(raw_data,
                [feature_words_vector, feature_mean_len_word,
                    feature_parts_of_speech])
        test_features_user_centric = compute_features(raw_data,
                [feature_meta])

        raw_proba_review_centric = cls_review_centric.predict_proba(test_features_review_centric)
        raw_proba_user_centric = cls_user_centric.predict_proba(test_features_user_centric)

        certain_good_indices = [i for i in range(len(raw_data)) if 
                raw_proba_review_centric[i][0] > MIN_PROBA and
                raw_proba_user_centric[i][0] > MIN_PROBA]
        certain_paid_indices = [i for i in range(len(raw_data)) if 
                raw_proba_review_centric[i][1] > MIN_PROBA and
                raw_proba_user_centric[i][1] > MIN_PROBA]
        print('Number of new certain good reviews: {}'.format(len(certain_good_indices)))
        print('Number of new certain paid reviews: {}'.format(len(certain_paid_indices)))

        new_good_reviews = raw_data[certain_good_indices]
        new_paid_reviews = raw_data[certain_paid_indices]

        mask = numpy.ma.array(raw_data, mask=True)
        mask[certain_good_indices] = False
        mask[certain_paid_indices] = False
        raw_data = raw_data[mask]

        cur_data_good += new_good_reviews
        cur_data_paid += new_paid_reviews

        if len(certain_good_indices) + len(certain_paid_indices) == 0:
            break


    with open('{}/result_data_good.json', 'w') as result_good:
        json.dump(cur_data_good, result_good)

    with open('{}/result_data_paid.json', 'w') as result_paid:
        json.dump(cur_data_paid, result_paid)
