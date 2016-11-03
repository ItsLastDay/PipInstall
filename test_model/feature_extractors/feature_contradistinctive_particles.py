import re

def json_to_text(json):
    return json.get('text', '') + '\n' + json.get('pro', '') + '\n' + json.get('contra', '')

# возможно, надо будет результат на что-то поделить, чтобы нормировать его,
# так как сейчас взнос фичи зависит от длины предложения
def feature_contradistinctive_particles(reviews_array):
    features = []

    contradistinctions = [' впрочем ', ' однако ', ' а ', ' но ', ' да ', ' зато ', ' все же ', ' тем не менее ',
                          ' как бы то ни было ', ' все таки ', ' опять таки ', ' ведь ', ' вместе с тем ',
                          ' во всяком случае ', ' все ж таки ', ' как ни говори ', ' как ни говорите ',
                          ' что ни говори ', ' что ни говорите ', ' при всем при том ', ' при всем том ',
                          ' как никак ', ' хотя ']

    def get_punctuation_count(string_review):

        punctuation_signs = re.split('[\w\s]', string_review)
        # filter empty strings
        punctuation_signs = [x for x in punctuation_signs if len(x) > 0]

        number_of_punctuation_signs = len(punctuation_signs)

        return number_of_punctuation_signs

    def get_contradestinctions_count(string_review):

        number_of_contradistinctions = 0

        string_review = string_review.lower()

        string_review = re.sub('[^a-zа-яё]', ' ', string_review)

        string_review += " "

        for item in contradistinctions:
            number_of_contradistinctions += string_review.count(item)

        return number_of_contradistinctions

    def helper(string_review):

        number_of_contradistinctions = 0

        number_of_contradistinctions += get_punctuation_count(string_review)

        number_of_contradistinctions += get_contradestinctions_count(string_review)

        return number_of_contradistinctions

    for review in reviews_array:
        features.append([
            helper(json_to_text(review))
        ])

    return features


# import json
# print(feature_contradistinctive_particles([json.loads('{"text":"дирижабль","grade":2,"delivery":"DELIVERY","id":66186256,"authorInfo":{"grades":1,"uid":431432957},"shop":{"id":76616,"name":"Cifrovoi.com"},"author":"Чадович Андрей","contra":"Отсутствуют","comments":[],"agree":0,"date":1477849186000,"shopId":76616,"reject":0,"shopOrderId":"75990","anonymous":false,"visibility":"NAME","region":2,"pro":"Хорошее обслуживание"}')]))
