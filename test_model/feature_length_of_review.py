import re
from pymystem3 import Mystem

def json_to_text(json):
    return json.get('text', '') + '\n' + json.get('pro', '') + '\n' + json.get('contra', '')

def feature_length_of_review(reviews_array):
    features = []
    m = Mystem()

    def helper(string_review):
        length = 0
        review_splitted_by_any_non_word_char = re.split('[^A-Za-zА-Яа-яёЁ]', string_review)
        for word in review_splitted_by_any_non_word_char:
            lemmatized = m.lemmatize(word)
            length += 0 if lemmatized == [] else len(lemmatized[0])

        return length

    for review in reviews_array:
        features.append([
            helper(json_to_text(review))
        ])

    return features

# import json
# print(feature_length_of_review([json.loads('{"text":"ХОРОШИЙ персонал жопа ,но КАК-НИКАК ;; ... ЧЕТКО все рассказывают, пусечкам все понятно,а главное,что лишние вопросы не возникают","grade":2,"delivery":"DELIVERY","id":66186256,"authorInfo":{"grades":1,"uid":431432957},"shop":{"id":76616,"name":"Cifrovoi.com"},"author":"Чадович Андрей","contra":"Отсутствуют","comments":[],"agree":0,"date":1477849186000,"shopId":76616,"reject":0,"shopOrderId":"75990","anonymous":false,"visibility":"NAME","region":2,"pro":"Хорошее обслуживание"}')]))
