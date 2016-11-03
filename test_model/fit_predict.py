import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold


def main():
    # json = load_reviews()
    # json = json['good'] + json['paid']
    # texts = [lemmatize_text(text) for text in json_to_texts(json)]
    #
    # X_train_vect = vectorize_texts(texts)
    # np.save('computed_features/feature_words_vector', X_train_vect)
    #
    # X_train_typos = count_all_typos(texts)
    # np.save('computed_features/feature_spelling', X_train_typos)

    features = ['get_features_synonim',
                'feature_caps_words', 'feature_contradistinctive_particles', 'feature_firstperson',
                'feature_length_of_review', 'feature_parts_of_speech', 'feature_unigrams_bigrams',
                'get_features_mean_len_word', 'get_features_meta', 'get_features_number_exclamation']

    X_train = np.hstack((np.load('computed_features/{}.npy'.format(feature))
                         for feature in features))

    Y_train = np.array([0 for _ in range(302)] + [1 for _ in range(302)])

    X_predict = np.hstack((np.load('computed_features_test/{}.npy'.format(feature))
                         for feature in features))

    cls = RandomForestClassifier(max_depth=10, n_estimators=250, random_state=42)

    cls.fit(X_train, Y_train)
    result = cls.predict(X_predict)


    print(result)
    print(len(result))


if __name__ == '__main__':
    main()
