
def get_features_number_exclamation(reviews_array, texts):
    features = []
    for review in reviews_array:
        count_excl = 0
        count_excl += review.get('text', '').count("!") + review.get('text', '').count(":)") + review.get('text', '').count(")") +  review.get('text', '').count(":-)")
        count_excl += review.get('pro', '').count("!") + review.get('pro', '').count(":)") + review.get('pro', '').count(")") +  review.get('pro', '').count(":-)")
        count_excl += review.get('contra', '').count("!") + review.get('contra', '').count(":)") + review.get('contra', '').count(")") +  review.get('contra', '').count(":-)")
        features.append([count_excl]) if count_excl == 0 else features.append([count_excl / len((review.get('text', '') +  review.get('pro', '') + review.get('contra', '')).split(' '))])          
    return features





