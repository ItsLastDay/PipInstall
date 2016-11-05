def get_features_mean_len_word(reviews_array, texts):
    features = []
    for text in texts:
        features.append([0])
        count_words = 0
        for lemma in text.split(' '):
            if lemma.isalnum():
                features[-1][0] += len(lemma)
                count_words += 1
        if count_words != 0:
            features[-1][0] /= count_words
        
    return features



