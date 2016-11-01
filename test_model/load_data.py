#!/usr/bin/env python3

import os.path
import json

DATA_FOLDER = '../data'
REVIEWS_PREFIX = 'reviews'

def load_reviews():
    reviews = dict()
    for review_type in ('good', 'paid'):
        review_filename = '{}_{}.json'.format(REVIEWS_PREFIX, review_type)
        reviews_path = os.path.join(DATA_FOLDER, review_filename)

        with open(reviews_path, 'r') as review_file:
            reviews[review_type] = json.load(review_file)

    return reviews
