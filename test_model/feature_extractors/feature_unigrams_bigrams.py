import re

def json_to_text(json):
    return json.get('text', '') + '\n' + json.get('pro', '') + '\n' + json.get('contra', '')

def feature_unigrams_bigrams(reviews_array, texts):
    features = []
    grams_map = {}
    cyrillic_base_unicode = 0x0430

    # init unigrams and bigrams map
    for i in range(32):
        grams_map[chr(cyrillic_base_unicode + i)] = i
        for j in range(32):
            grams_map[str(chr(cyrillic_base_unicode + i)) + str(chr(cyrillic_base_unicode + j))] = 32 * (i + 1) + j

    def helper(string_review):

        grams_vector = [0]*(32*32 + 32)

        string_review = re.sub('[^а-я]', '', string_review.lower())

        for i in range(len(string_review)):
            grams_vector[grams_map[string_review[i]]] += 1

        for i in range(len(string_review) - 1):
            grams_vector[grams_map[string_review[i:i+2]]] += 1

        return grams_vector

    for review in reviews_array:
        data = helper(json_to_text(review))
        features.append(data)

    return features


# import json
# print(feature_unigrams_bigrams([json.loads('{"text":"абвгдеёжзийклмнопрстуфхцчшщъыьэюя","grade":2,"delivery":"DELIVERY","id":66186256,"authorInfo":{"grades":1,"uid":431432957},"shop":{"id":76616,"name":"Cifrovoi.com"},"author":"Чадович Андрей","comments":[],"agree":0,"date":1477849186000,"shopId":76616,"reject":0,"shopOrderId":"75990","anonymous":false,"visibility":"NAME","region":2,"pro":""}')]))
