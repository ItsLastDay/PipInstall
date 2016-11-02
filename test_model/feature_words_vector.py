import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from pymystem3 import Mystem

from sklearn.ensemble import RandomForestClassifier

from load_data import load_reviews
from test_classifier import perform_crossval

from sklearn.model_selection import cross_val_score, StratifiedKFold


def lemmatize_text(text):
    m = Mystem()
    return ' '.join(word for word in m.lemmatize(text) if all(ch.isalpha() for ch in word))


def json_to_texts(json):
    return [r.get('text', '') + '\n' + r.get('pro', '') + '\n' + r.get('contra', '')
            for r in json]


def vectorize_texts(texts):
    X_train = [lemmatize_text(text) for text in texts]
    vectorizer = CountVectorizer(encoding='koi8r', stop_words=stopwords.words('russian'), max_features=256)
    return vectorizer.fit_transform(X_train).toarray()


def main():
    reviews = load_reviews()

    flat_reviews = reviews['good'] + reviews['paid']
    X_train_json = json_to_texts(flat_reviews)
    X_train_vect = vectorize_texts(X_train_json)

    y = [0 for _ in range(len(reviews['good']))] + \
        [1 for _ in range(len(reviews['paid']))]
    y = np.array(y)

    cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    scores = cross_val_score(RandomForestClassifier(n_estimators=300, random_state=42),
                             X_train_vect, y, scoring='accuracy', cv=cv)

    print(scores)


if __name__ == '__main__':
    main()
