import re


def feature_contradistinctive_particles(reviews_array):
    features = []

    contradistinctions = ['впрочем', 'однако', 'а', 'но', 'да', 'зато', 'все же', 'тем не менее', 'как бы то ни было',
                          'все-таки', 'опять-таки', 'ведь', 'вместе с тем', 'во всяком случае', 'все ж таки',
                          'как ни говори', 'как ни говорите', 'что ни говори', 'что ни говорите', 'при всем при том',
                          'при всем том', 'как-никак', 'хотя']

    def helper(string_review):

        number_of_contradistinctions = 0

        punctuation_signs = re.split('[\w\s]', string_review)
        # filter empty strings
        punctuation_signs = [x for x in punctuation_signs if len(x) > 0]
        number_of_punctuation_signs = len(punctuation_signs)

        number_of_contradistinctions += number_of_punctuation_signs

        review_split_by_any_non_word_char = re.split('[^A-Za-zА-Яа-яёЁ]', string_review)

        for word in review_split_by_any_non_word_char:
            number_of_contradistinctions += word.lower() in contradistinctions

        return number_of_contradistinctions

    for review in reviews_array:
        features.append([
            helper(review['text']) + helper(review['pro']) + helper(review['contra'])
        ])

    return features


# import json
# print(feature_contradistinctive_particles([json.loads('{"text":"ХОРОШИЙ персонал,но КАК-НИКАК ;; ... ЧЕТКО все рассказывают,все понятно,а главное,что лишние вопросы не возникают","grade":2,"delivery":"DELIVERY","id":66186256,"authorInfo":{"grades":1,"uid":431432957},"shop":{"id":76616,"name":"Cifrovoi.com"},"author":"Чадович Андрей","contra":"Отсутствуют","comments":[],"agree":0,"date":1477849186000,"shopId":76616,"reject":0,"shopOrderId":"75990","anonymous":false,"visibility":"NAME","region":2,"pro":"Хорошее обслуживание"}')]))
