#!/usr/bin/env python3

'''
Count statistics about input .json file with reviews:
    - number of entries
    - number of reviews with grade < 4

Input:
    1 = path to .json file
'''

import json
import sys


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as json_input:
        review_data = json.load(json_input)

        num_of_entries = len(review_data)

        num_negative_reviews = len([x['grade'] for x in review_data \
                if x['grade'] < 1]) # Y.market grades are -2..2

        print('Number of entries: {}'.format(num_of_entries))
        print('Number of negative reviews: {}'.format(num_negative_reviews))
