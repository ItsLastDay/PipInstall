#!/usr/bin/env python3

import os
import json
import codecs

DATA_FOLDER = '../../data/assessing_results/'

votes_map = {}
reviews_map = {}

merged_good = []
merged_bad = []

def handle_good(reviews_json):
    for review in reviews_json:
        if review.get("id") in votes_map:
            votes_map[review.get("id")] += 1
        else:
            reviews_map[review.get("id")] = review
            votes_map[review.get("id")] = 1


def handle_bad(reviews_json):
    for review in reviews_json:
        if review.get("id") in votes_map:
            votes_map[review.get("id")] -= 1
        else:
            reviews_map[review.get("id")] = review
            votes_map[review.get("id")] = -1


for file in os.listdir(DATA_FOLDER):
    if file.endswith(".txt"):
        if file.find("not_truthful") != -1:
            with open(DATA_FOLDER + file) as bad_reviews:
                handle_bad(json.load(bad_reviews))
        elif file.find("truthful") != -1:
            with open(DATA_FOLDER + file) as good_reviews:
                handle_good(json.load(good_reviews))


for review_id in votes_map:
    if votes_map[review_id] >= 2:
        merged_good.append(reviews_map[review_id])
    elif votes_map[review_id] <= -2:
        merged_bad.append(reviews_map[review_id])


good_file = codecs.open(DATA_FOLDER + "merged_good.txt", 'w+', 'utf-8')
bad_file = codecs.open(DATA_FOLDER + "merged_bad.txt", 'w+', 'utf-8')

json.dump(merged_good, good_file, ensure_ascii=False)
good_file.close()

json.dump(merged_bad, bad_file, ensure_ascii=False)
bad_file.close()

