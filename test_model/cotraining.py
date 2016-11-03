#!/usr/bin/env python3

import json
import numpy

from load_data import load_reviews
from feature_extractors import *
from test_classifier import compute_features

import sklearn.naive_bayes

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

        features_review_centric = compute_features(flat_reviews,
                [feature_words_vector, feature_mean_len_word,
                    feature_firstperson])

    with open('{}/result_data_good.json', 'w') as result_good:
        json.dump(cur_data_good, result_good)

    with open('{}/result_data_paid.json', 'w') as result_paid:
        json.dump(cur_data_paid, result_paid)
