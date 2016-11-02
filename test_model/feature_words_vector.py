import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from pymystem3 import Mystem
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold

m = Mystem()


def lemmatize_text(text):
    return ' '.join(word for word in m.lemmatize(text) if all(ch.isalpha() for ch in word))


def json_to_texts(json):
    return [r.get('text', '') + '\n' + r.get('pro', '') + '\n' + r.get('contra', '')
            for r in json]


def vectorize_texts(texts):
    vectorizer = CountVectorizer(encoding='koi8r', stop_words=stopwords.words('russian'), max_features=256)
    return vectorizer.fit_transform(texts).toarray()


def main():
    features = ['X_train_vect', 'X_train_typos', 'feature_firstperson']
    X_train = np.hstack((np.load('computed_features/{}.npy'.format(feature))
                         for feature in features))
    y_train = np.array([0 for _ in range(302)] + [1 for _ in range(302)])

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scores = cross_val_score(RandomForestClassifier(max_depth=10, n_estimators=250, random_state=42),
                             X_train, y_train, scoring='accuracy', cv=cv)

    print(scores.mean())


if __name__ == '__main__':
    main()
