#!/usr/bin/env python3

import json
import numpy as np

from load_data import load_reviews
from feature_extractors import *
from test_classifier import compute_features

import sklearn.naive_bayes

MIN_PROBA = 0.95
COTRAIN_FOLDER = '../data/cotraining_data'

if __name__ == '__main__':
    print('Welcome to cotraining!')

    seed_data = load_reviews(folder=COTRAIN_FOLDER, prefix='seed')

    raw_data = json.load(open('{}/raw_data.json'.format(COTRAIN_FOLDER), 'r'))
    # Only results with grade >= 4 (which is >= 1 in -2..2). 
    raw_data = list(filter(lambda x: x['grade'] >= 1, raw_data))
    raw_data = np.array(raw_data)

    cur_data_good = seed_data['good']
    cur_data_paid = seed_data['paid']

    # Assuming that paid data is always less
    min_sz = len(cur_data_paid)
    lefotver_good_data = cur_data_good[min_sz:]
    cur_data_good = cur_data_good[:min_sz]

    print('Raw data has length {}'.format(len(raw_data)))
    print('Good data has length {}'.format(len(cur_data_good)))
    print('Paid data has length {}'.format(len(cur_data_paid)))
    print('Leftover good has length {}'.format(len(lefotver_good_data)))

    number_of_added_good_so_far = 0
    number_of_added_paid_so_far = 0

    it = 0
    while True:
        print('\n\nIteration {}'.format(it))
        cls_review_centric = sklearn.naive_bayes.MultinomialNB()
        cls_user_centric = sklearn.naive_bayes.GaussianNB()

        flat_reviews = cur_data_good + cur_data_paid
        flat_reviews = np.array(flat_reviews)

        labels = [0 for i in range(len(cur_data_good))] +\
                [1 for i in range(len(cur_data_paid))]

        words_vector = FeatureWordsVector()
        feature_words_vector = lambda x: words_vector(x, True)

        # Train two classifiers on distinc features.
        train_features_review_centric = compute_features(flat_reviews,
                [feature_words_vector,
                    get_features_number_exclamation])
        train_features_user_centric = compute_features(flat_reviews,
                [get_features_meta])

        cls_review_centric.fit(train_features_review_centric, labels)
        cls_user_centric.fit(train_features_user_centric, labels)


        # Get features for raw data.
        feature_words_vector = lambda x: words_vector(x, False)
        test_features_review_centric = compute_features(raw_data,
                [feature_words_vector,
                    get_features_number_exclamation])
        test_features_user_centric = compute_features(raw_data,
                [get_features_meta])

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
        #print([(i, raw_proba_review_centric[i]) for i in certain_good_indices])

        number_of_added_good_so_far += len(certain_good_indices)
        number_of_added_paid_so_far += len(certain_paid_indices)

        new_good_reviews = raw_data[certain_good_indices]
        new_paid_reviews = raw_data[certain_paid_indices]

        raw_data = [x for i, x in enumerate(raw_data) if i not in certain_good_indices 
                and i not in certain_paid_indices]
        raw_data = np.array(raw_data)
        print('Now raw_data is of length {}'.format(len(raw_data)))

        cur_data_good.extend(new_good_reviews)
        cur_data_paid.extend(new_paid_reviews)

        print('Number of added good so far: {}'.format(number_of_added_good_so_far))
        print('Number of added paid so far: {}'.format(number_of_added_paid_so_far))

        if len(certain_good_indices) + len(certain_paid_indices) == 0:
            break
        it += 1

    if len(cur_data_good) < len(cur_data_paid):
        cur_data_good.extend(lefotver_good_data[:len(cur_data_paid) - len(cur_data_good)])
    print('Final number of good reviews: {}'.format(len(cur_data_good)))
    print('Final number of paid reviews: {}'.format(len(cur_data_paid)))

    with open('{}/result_data_good.json'.format(COTRAIN_FOLDER), 'w') as result_good:
        json.dump(cur_data_good, result_good)

    with open('{}/result_data_paid.json'.format(COTRAIN_FOLDER), 'w') as result_paid:
        json.dump(cur_data_paid, result_paid)
