import requests


def send_request(shop_id, count, key, frmt='json'):
    url = "https://api.content.market.yandex.ru/v1/shop/{}/opinion.{}?count={}".format(shop_id, frmt, count)
    headers = {'Authorization': key, 'Accept': '*/*'}

    response = requests.get(url, headers=headers)
    json_object = response.json()
    if 'errors' in json_object:
        print(json_object['errors'])
        return

    models = json_object['searchResult']['results']
    print(models)


def main():
    send_request(98576, 10, 'a41349df4aa24293a77cc6db6dd96ed1')


if __name__ == '__main__':
    main()
