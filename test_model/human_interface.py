#!/usr/bin/env python3
from classifier_interface import Classifier
import requests
import json

cls = Classifier()

def get_comments(shop_id, count, page, key, sort, frmt='json'):
    url = "https://api.content.market.yandex.ru/v1/shop/{}/opinion.{}?page={}&count={}&how=desc&sort={}"\
        .format(shop_id, frmt, page, count, sort)
    headers = {'Authorization': key, 'Accept': '*/*'}

    response = requests.get(url, headers=headers)
    json_object = response.json()
    if 'errors' in json_object:
        print(json_object['errors'])
        return None

    return json_object['shopOpinions']['opinion']

while True:
    '''
    Sample input:
    5557
    1
    date

    https://market.yandex.ru/shop/5557/reviews?suggest_text=SLK-Service.ru%20%D0%BE%D1%82%D0%B7%D1%8B%D0%B2%D1%8B&suggest_type=shop&sort_by=date
    '''
    print('\n\n')
    shop_id = input('Введите id магазина: ')
    count = 10
    page = input('Введите номер страницы: ')
    sort = input('Введите тип сортировки (date, grade, rank): ')
    
    comments = get_comments(shop_id, count, page, 'T9hQjm9W7BjYfWnsfkZZUwxRAKdklO', sort)

    answers = cls.predict_json(comments)

    for answer, comment in zip(answers, comments):
        print('\n\n')
        print('*' * 80)
        print('Review id: {}'.format(comment['id']))
        print('Review text:')
        print('Достоинства: {}'.format(comment.get('pro', '------')))
        print('Недостатки: {}'.format(comment.get('contra', '-----')))
        print('Комментарий: {}'.format(comment.get('text', '------')))
        print('\nClassifier verdict:')
        print(answer)




