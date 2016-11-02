import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold

from load_data import load_reviews
from feature_words_vector import json_to_texts, lemmatize_text, vectorize_texts
from feature_spelling import count_all_typos


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

    features = ['feature_words_vector', 'feature_spelling', 'get_features_synonim',
                'feature_caps_words', 'feature_contradistinctive_particles', 'feature_firstperson',
                'feature_length_of_review', 'feature_parts_of_speech', 'feature_unigrams_bigrams',
                'get_features_mean_len_word', 'get_features_meta', 'get_features_number_exclamation']
    X_train = np.hstack((np.load('computed_features/{}.npy'.format(feature))
                         for feature in features))
    y_train = np.array([0 for _ in range(302)] + [1 for _ in range(302)])

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scores = cross_val_score(RandomForestClassifier(max_depth=10, n_estimators=250, random_state=42),
                             X_train, y_train, scoring='accuracy', cv=cv)

    print(scores.mean())


if __name__ == '__main__':
    main()
