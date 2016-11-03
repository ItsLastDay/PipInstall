import re

def json_to_text(json):
    return json.get('text', '') + '\n' + json.get('pro', '') + '\n' + json.get('contra', '')

def feature_caps_words(reviews_array):
    features = []

    def helper(string_review):
        number_of_caps_words = 0
        review_splitted_by_any_non_word_char = re.split('[^A-Za-zА-Яа-яёЁ]', string_review)
        length = len(review_splitted_by_any_non_word_char)
        for word in review_splitted_by_any_non_word_char:
            if word.isupper():
                number_of_caps_words += 1

        return number_of_caps_words / length

    for review in reviews_array:
        features.append([
            helper(json_to_text(review))
        ])

    return features


# import json
# print(feature_caps_words([json.loads('{"text":" персонал, ПРОПА но  ;; ...  все рассказывают,все понятно,а главное,что лишние вопросы не возникают","grade":2,"delivery":"DELIVERY","id":66186256,"authorInfo":{"grades":1,"uid":431432957},"shop":{"id":76616,"name":"Cifrovoi.com"},"author":"Чадович Андрей","comments":[],"agree":0,"date":1477849186000,"shopId":76616,"reject":0,"shopOrderId":"75990","anonymous":false,"visibility":"NAME","region":2,"pro":""}')]))
