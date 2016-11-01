import requests
import json


def get_comments(shop_id, count, page, key, frmt='json'):
    url = "https://api.content.market.yandex.ru/v1/shop/{}/opinion.{}?page={}&count={}&how=desc"\
        .format(shop_id, frmt, page, count)
    headers = {'Authorization': key, 'Accept': '*/*'}

    response = requests.get(url, headers=headers)
    json_object = response.json()
    if 'errors' in json_object:
        print(json_object['errors'])
        return None

    return json_object['shopOpinions']['opinion']


def main():
    opinions = []

    shop_ids = [211, 42315, 37758, 3678, 76616, 78300, 18196, 242112, 48260, 5557, 359037]
    for shop_id in shop_ids:
        for i_page in range(1, 6):
            opinions += get_comments(shop_id, 20, i_page, 'T9hQjm9W7BjYfWnsfkZZUwxRAKdklO')

    with open('data.json', 'w') as f:
        json.dump(opinions, f, ensure_ascii=False)

    print(len(opinions))


if __name__ == '__main__':
    main()
