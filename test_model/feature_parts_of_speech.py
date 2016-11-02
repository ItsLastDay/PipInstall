import re
from pymystem3 import Mystem

def json_to_text(json):
    return json.get('text', '') + '\n' + json.get('pro', '') + '\n' + json.get('contra', '')

def feature_parts_of_speech(reviews_array):
    features = []
    grams_map = {}
    parts_of_speech = ['A', 'ADV', 'ADVPRO', 'ANUM', 'APRO', 'COM', 'CONJ', 'INTJ', 'NUM', 'PART', 'PR', 'S', 'SPRO', 'V']
    length_parts = len(parts_of_speech)
    m = Mystem()

    # init unigrams and bigrams map
    for i in range(length_parts):
        grams_map[parts_of_speech[i]] = i
        for j in range(length_parts):
            grams_map[parts_of_speech[i] + " " + parts_of_speech[j]] = length_parts * (i + 1) + j

    def translate_to_parts(string_review):

        parts = []

        string_review = re.sub('[^а-я]', ' ', string_review.lower())

        only_parts = m.analyze(string_review)

        for part in only_parts:
            if 'analysis' in part:
                gr = part['analysis'][0]['gr']
                parts.append(re.search('^[A-Z]+', gr).group())


        return parts

    def helper(string_review):

        grams_vector = [0]*(length_parts*length_parts + length_parts)

        translated_review = translate_to_parts(string_review)

        for i in range(len(translated_review)):
            grams_vector[grams_map[translated_review[i]]] += 1

        for i in range(len(translated_review) - 1):
            grams_vector[grams_map[" ".join(translated_review[i:i+2])]] += 1

        return grams_vector

    for review in reviews_array:

        features.append(helper(json_to_text(review)))

    return features


# import json
# print(feature_parts_of_speech([json.loads('{"text":"хороший хороший","grade":2,"delivery":"DELIVERY","id":66186256,"authorInfo":{"grades":1,"uid":431432957},"shop":{"id":76616,"name":"Cifrovoi.com"},"author":"Чадович Андрей","contra":"","comments":[],"agree":0,"date":1477849186000,"shopId":76616,"reject":0,"shopOrderId":"75990","anonymous":false,"visibility":"NAME","region":2,"pro":""}')]))
