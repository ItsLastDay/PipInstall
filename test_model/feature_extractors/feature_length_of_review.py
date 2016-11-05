import re

def json_to_text(json):
    return json.get('text', '') + '\n' + json.get('pro', '') + '\n' + json.get('contra', '')

def feature_length_of_review(reviews_array, texts):
    features = []

    def helper(text):
        length = 0
        for word in text.split(' '):
            lemmatized = word
            length += len(lemmatized)

        return length

    for text in texts:
        features.append([
            helper(text)
        ])

    return features

# import json
# print(feature_length_of_review([json.loads('{"text":"ХОРОШИЙ персонал жопа ,но КАК-НИКАК ;; ... ЧЕТКО все рассказывают, пусечкам все понятно,а главное,что лишние вопросы не возникают","grade":2,"delivery":"DELIVERY","id":66186256,"authorInfo":{"grades":1,"uid":431432957},"shop":{"id":76616,"name":"Cifrovoi.com"},"author":"Чадович Андрей","contra":"Отсутствуют","comments":[],"agree":0,"date":1477849186000,"shopId":76616,"reject":0,"shopOrderId":"75990","anonymous":false,"visibility":"NAME","region":2,"pro":"Хорошее обслуживание"}')]))
