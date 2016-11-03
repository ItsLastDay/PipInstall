
#[id магазина, анализ имени автора по шкале 1-3, длина имени автора, анонимность отзыва, количество оставленных автором отзывов]

def analyse_name(name):
    if name.count(' ') == 1 and name.istitle():
        return 3
    elif name.find(' ') != -1 or name.count('.') == 1 or name.count('_') == 1:
        return 2
    else:
        return 1

def get_features_meta(reviews_array):
    features = []
    for review in reviews_array:
        elem = []
        elem.append(review['shopId'])
        elem.append(analyse_name(review.get('author', '')))
        elem.append(len(review.get('author', '')))
        elem.append(review['anonymous'])
        elem.append(review.get('authorInfo',{}).get('grades',0))
        features.append(elem)
    return features




