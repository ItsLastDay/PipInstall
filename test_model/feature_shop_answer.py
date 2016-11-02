
def get_features_shop_answer(reviews_array):
    features = []
    for review in reviews_array:
        features.append([0])
        if len(review['comments']) != 0:
            for comment in review['comments']:
                if comment['user'].get('name', '').find('Ответ магазина') != -1:
                    features[len(features) - 1][0] = 1
                    break
    return features




