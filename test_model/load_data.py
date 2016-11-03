import os.path
import json

DATA_FOLDER = '../data'
REVIEWS_PREFIX = 'reviews'


def load_reviews(folder=DATA_FOLDER, prefix=REVIEWS_PREFIX):
    reviews = dict()
    for review_type in ('good', 'paid'):
        review_filename = '{}_{}.json'.format(prefix, review_type)
        reviews_path = os.path.join(folder, review_filename)

        with open(reviews_path, 'r') as review_file:
            reviews[review_type] = json.load(review_file)

    return reviews
