#!/usr/bin/env python3

import argparse
import pickle
import sys

from matplotlib import pyplot

import sklearn.manifold
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn import metrics
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from pymystem3 import Mystem

from load_data import load_reviews

from feature_extractors import *

mstem = Mystem()

def lemmatize_text(text):
    return ' '.join(word for word in mstem.lemmatize(text) if all(ch.isalpha() for ch in word))


def json_to_texts(json):
    return [r.get('text', '') + '\n' + r.get('pro', '') + '\n' + r.get('contra', '')
            for r in json]

def compute_features(reviews, feature_funcs, dump=False):
    features = [[] for i in range(len(reviews))]
    texts = [lemmatize_text(text) for text in json_to_texts(reviews)]

    for feature_func in feature_funcs:
        cur_features = feature_func(reviews, texts)
        for i in range(len(reviews)):
            features[i].extend(cur_features[i])

    features = np.array(features)

    if dump:
        dump_name = './computed_features/' + ','.join(map(lambda f: f.__name__, feature_funcs)) + '.npy'
        with open(dump_name, 'wb') as dump_file:
            np.save(dump_name, features)

    return features


def perform_crossval(reviews, labels, clf, metric=lambda x, y: 1,
                     feature_funcs=None, print_features=0, visualize=False):
    '''
    Perform cross validation on reviews.

    `metric` is a function <true_labels, predicted_labels> -> <float score>.

    Each element of `feature_funcs` is a function
        <array of reviews> -> <list of features>
    '''
    feature_funcs = feature_funcs or []
    features = compute_features(reviews, feature_funcs)

    if print_features > 0:
        print('First {} features (for good reviews):'.format(print_features))
        print(features[:print_features])
        print('Last {} features (for paid reviews):'.format(print_features))
        print(features[-print_features:])

    if visualize:
        tsne = sklearn.manifold.TSNE(perplexity=20, n_iter=5000)
        twod_points = tsne.fit_transform(features)

        colors = ['red' if x == 0 else 'green' for x in labels]
        pyplot.scatter(twod_points[:, 0], twod_points[:, 1], c=colors)
        pyplot.show()

    cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    scores = cross_val_score(clf, features, labels, scoring=metrics.make_scorer(metric), cv=cv)

    return scores.mean()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dump-all', default=False, action='store_true',
                        dest='test_all')
    parser.add_argument('--print-features', type=int, default=0,
                        dest='print_features')
    parser.add_argument('--visualize', default=False, action='store_true',
                        dest='visualize')
    args = parser.parse_args()

    # Load reviews as dict with two keys: 'good' and 'paid'.
    reviews = load_reviews(folder='../data/cotraining_data/', prefix='result_data')

    # Preprocess all reviews, return two arrays if length n:
    # 1. vector of features for each object,
    # 2. label for each object (0 - good, 1 - paid).
    flat_reviews = reviews['good'] + reviews['paid']
    labels = [0 for i in range(len(reviews['good']))] + \
             [1 for i in range(len(reviews['paid']))]

    labels = np.array(labels)

    if args.test_all:
        word_vector = FeatureWordsVector()
        def feature_words_vector(reviews):
            return word_vector(reviews, True)
        feature_funcs = [
                get_features_number_exclamation,
                get_features_meta,
                get_features_synonim,
                get_features_mean_len_word,
                feature_caps_words,
                feature_contradistinctive_particles,
                feature_firstperson,
                feature_length_of_review,
                feature_parts_of_speech,
                feature_unigrams_bigrams,
                feature_words_vector
                ]
        print('Computing and saving features')
        for i, func in enumerate(feature_funcs):
            f = func
            print(i + 1, f.__name__)
            compute_features(flat_reviews, [f], dump=True)

        sys.exit(0)

    word_vector = FeatureWordsVector()
    feature_words_vector = lambda x: word_vector(x, True)

    scores = perform_crossval(flat_reviews, labels, RandomForestClassifier(n_estimators=300, random_state=42),
                              metric=metrics.accuracy_score,
                              feature_funcs=[feature_contradistinctive_particles, feature_unigrams_bigrams, feature_firstperson, get_features_synonim, get_features_number_exclamation, feature_length_of_review, feature_caps_words, get_features_meta, get_features_mean_len_word, feature_words_vector], print_features=args.print_features,
                              visualize=args.visualize)

    print(scores)
