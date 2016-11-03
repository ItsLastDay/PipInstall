#!/usr/bin/env python3

import os
import json
import os.path
import random
import argparse

assessed_results_dir = './assessing_results'

def get_review_data(json_filenames):
    review_data = []

    for json_filename in json_filenames:
        with open(json_filename, 'r') as json_data:
            review_data.extend(json.load(json_data))

    return review_data

TEST_SIZE = 50

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gen-seed-cotraining', action='store_true')
    parser.add_argument('--split-train-test', action='store_true')
    args = parser.parse_args()


    result_files = list(map(lambda name:
        os.path.abspath(os.path.join(assessed_results_dir, name)), 
        os.listdir(assessed_results_dir)))

    truthful_names = list(filter(lambda x: 'merged_good.txt' in x,
            result_files))
    not_truthful_names = list(filter(lambda x: 
            'merged_bad.txt' in x,
            result_files))

    truthful_data = get_review_data(truthful_names)
    not_truthful_data = get_review_data(not_truthful_names)

    print('Total number of good reviews: {}'.format(len(truthful_data)))
    print('Total number of paid reviews: {}'.format(len(not_truthful_data)))

    random.shuffle(truthful_data)
    random.shuffle(not_truthful_data)

    sz_min_set = min(len(truthful_data), len(not_truthful_data))

    if args.split_train_test:
        # Put TEST_SIZE reviews of each class into Test set (evaluated in the end)
        with open('./test_reviews_good.json', 'w') as test_reviews_good:
            json.dump(truthful_data[:TEST_SIZE], test_reviews_good)
        with open('./test_reviews_paid.json', 'w') as test_reviews_paid:
            json.dump(not_truthful_data[:TEST_SIZE], test_reviews_paid)

        # Put `sz_min_set` - TEST_SIZE reviews of each class into Training set
        with open('./reviews_good.json', 'w') as train_reviews_good:
            json.dump(truthful_data[-(sz_min_set - TEST_SIZE):], train_reviews_good)
        with open('./reviews_paid.json', 'w') as train_reviews_paid:
            json.dump(not_truthful_data[-(sz_min_set - TEST_SIZE):], train_reviews_paid)

    if args.gen_seed_cotraining:
        print('ENTER COTRAINING')
        # Put TEST_SIZE reviews of each class into Test set (evaluated in the end)
        with open('./test_reviews_good.json', 'w') as test_reviews_good:
            json.dump(truthful_data[:TEST_SIZE], test_reviews_good)
        with open('./test_reviews_paid.json', 'w') as test_reviews_paid:
            json.dump(not_truthful_data[:TEST_SIZE], test_reviews_paid)

        # Dump seed reviews for cotraining, use all remaining data. 
        with open('./cotraining_data/seed_good.json', 'w') as seed_good:
            json.dump(truthful_data[TEST_SIZE:], seed_good)
        with open('./cotraining_data/seed_paid.json', 'w') as seed_paid:
            json.dump(not_truthful_data[TEST_SIZE:], seed_paid)



