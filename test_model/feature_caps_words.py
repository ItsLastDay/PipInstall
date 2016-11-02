import re


def feature_caps_words(reviews_array):
    features = []

    def helper(string_review):
        number_of_caps_words = 0
        review_splitted_by_any_non_word_char = re.split('[^A-Za-zА-Яа-яёЁ]', string_review)
        for word in review_splitted_by_any_non_word_char:
            if word.isupper():
                number_of_caps_words += 1

        return number_of_caps_words

    for review in reviews_array:
        features.append([
            helper(review['text']) + helper(review['pro']) + helper(review['contra'])
        ])

    return features
